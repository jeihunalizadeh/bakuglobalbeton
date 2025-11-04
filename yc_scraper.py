#!/usr/bin/env python3
"""
Y Combinator Startup Scraper
Scrapes recently funded YC startups and extracts:
- Company name and description
- Product link
- Batch/funding information
- Founders and their social media accounts
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import re
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse
import sys

class YCStartupScraper:
    def __init__(self):
        self.base_url = "https://www.ycombinator.com"
        self.companies_url = f"{self.base_url}/companies"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.startups = []
        
    def fetch_page(self, url, retries=3):
        """Fetch a page with retry logic"""
        for attempt in range(retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                print(f"Attempt {attempt + 1} failed for {url}: {e}")
                if attempt < retries - 1:
                    time.sleep(2)
                else:
                    return None
        return None
    
    def extract_social_links(self, soup, company_url):
        """Extract social media links from company page"""
        social_links = {
            'linkedin': [],
            'twitter': [],
            'github': []
        }
        
        # Find all links on the page
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            
            if 'linkedin.com/in/' in href:
                social_links['linkedin'].append(href)
            elif 'twitter.com/' in href or 'x.com/' in href:
                social_links['twitter'].append(href)
            elif 'github.com/' in href and '/github.com/' in href:
                social_links['github'].append(href)
        
        # Remove duplicates
        for platform in social_links:
            social_links[platform] = list(set(social_links[platform]))
        
        return social_links
    
    def extract_founders_info(self, soup):
        """Extract founders information from company page"""
        founders = []
        
        # Look for founder sections (YC pages typically have founder info)
        founder_sections = soup.find_all(['div', 'section'], class_=re.compile(r'founder|team|people', re.I))
        
        for section in founder_sections:
            # Extract names and roles
            names = section.find_all(['h3', 'h4', 'span', 'div'], class_=re.compile(r'name|founder', re.I))
            for name_elem in names:
                name_text = name_elem.get_text(strip=True)
                if name_text and len(name_text) < 50:  # Reasonable name length
                    founders.append({
                        'name': name_text,
                        'role': 'Founder'
                    })
        
        return founders[:5]  # Limit to 5 founders max
    
    def scrape_company_details(self, company_url, company_name):
        """Scrape detailed information from individual company page"""
        print(f"  Fetching details for: {company_name}")
        
        response = self.fetch_page(company_url)
        if not response:
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        details = {
            'social_links': self.extract_social_links(soup, company_url),
            'founders': self.extract_founders_info(soup)
        }
        
        return details
    
    def scrape_companies_list(self, batch_filter=None, limit=50):
        """Scrape the main companies list page"""
        print(f"Fetching YC companies list from: {self.companies_url}")
        
        # YC uses a dynamic API endpoint for their companies
        api_url = "https://www.ycombinator.com/companies"
        
        response = self.fetch_page(api_url)
        if not response:
            print("Failed to fetch companies list")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # YC's website structure - look for company cards/links
        company_links = soup.find_all('a', href=re.compile(r'/companies/[^/]+$'))
        
        print(f"Found {len(company_links)} company links")
        
        processed = 0
        for link in company_links[:limit]:
            if processed >= limit:
                break
                
            company_path = link.get('href')
            company_url = urljoin(self.base_url, company_path)
            company_name = link.get_text(strip=True)
            
            if not company_name:
                # Try to extract from URL
                company_name = company_path.split('/')[-1].replace('-', ' ').title()
            
            # Extract basic info from the list page
            parent = link.find_parent(['div', 'article', 'section'])
            description = ""
            batch = ""
            
            if parent:
                # Try to find description
                desc_elem = parent.find(['p', 'div'], class_=re.compile(r'description|tagline', re.I))
                if desc_elem:
                    description = desc_elem.get_text(strip=True)
                
                # Try to find batch info
                batch_elem = parent.find(['span', 'div'], class_=re.compile(r'batch|year', re.I))
                if batch_elem:
                    batch = batch_elem.get_text(strip=True)
            
            startup_data = {
                'company_name': company_name,
                'description': description,
                'batch': batch,
                'company_url': company_url,
                'product_link': company_url,
                'founders': [],
                'social_links': {
                    'linkedin': [],
                    'twitter': [],
                    'github': []
                },
                'scraped_at': datetime.now().isoformat()
            }
            
            # Fetch detailed information (with rate limiting)
            time.sleep(1)  # Be respectful to the server
            details = self.scrape_company_details(company_url, company_name)
            
            if details:
                startup_data['founders'] = details.get('founders', [])
                startup_data['social_links'] = details.get('social_links', startup_data['social_links'])
            
            self.startups.append(startup_data)
            processed += 1
            print(f"  Processed {processed}/{limit}: {company_name}")
        
        print(f"\nTotal startups scraped: {len(self.startups)}")
    
    def save_to_json(self, filename='yc_startups.json'):
        """Save scraped data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.startups, f, indent=2, ensure_ascii=False)
        print(f"Data saved to {filename}")
    
    def save_to_csv(self, filename='yc_startups.csv'):
        """Save scraped data to CSV file"""
        if not self.startups:
            print("No data to save")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = [
                'company_name', 'description', 'batch', 'company_url', 
                'product_link', 'founders_names', 'linkedin_profiles', 
                'twitter_profiles', 'github_profiles', 'scraped_at'
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for startup in self.startups:
                row = {
                    'company_name': startup['company_name'],
                    'description': startup['description'],
                    'batch': startup['batch'],
                    'company_url': startup['company_url'],
                    'product_link': startup['product_link'],
                    'founders_names': '; '.join([f['name'] for f in startup['founders']]),
                    'linkedin_profiles': '; '.join(startup['social_links']['linkedin']),
                    'twitter_profiles': '; '.join(startup['social_links']['twitter']),
                    'github_profiles': '; '.join(startup['social_links']['github']),
                    'scraped_at': startup['scraped_at']
                }
                writer.writerow(row)
        
        print(f"Data saved to {filename}")
    
    def print_summary(self):
        """Print a summary of scraped data"""
        print("\n" + "="*60)
        print("SCRAPING SUMMARY")
        print("="*60)
        print(f"Total companies scraped: {len(self.startups)}")
        
        if self.startups:
            companies_with_founders = sum(1 for s in self.startups if s['founders'])
            companies_with_linkedin = sum(1 for s in self.startups if s['social_links']['linkedin'])
            companies_with_twitter = sum(1 for s in self.startups if s['social_links']['twitter'])
            
            print(f"Companies with founder info: {companies_with_founders}")
            print(f"Companies with LinkedIn links: {companies_with_linkedin}")
            print(f"Companies with Twitter links: {companies_with_twitter}")
            
            print("\nSample data (first 3 companies):")
            for i, startup in enumerate(self.startups[:3], 1):
                print(f"\n{i}. {startup['company_name']}")
                print(f"   Description: {startup['description'][:100]}...")
                print(f"   Batch: {startup['batch']}")
                print(f"   URL: {startup['company_url']}")
                print(f"   Founders: {len(startup['founders'])}")
                print(f"   LinkedIn: {len(startup['social_links']['linkedin'])}")
                print(f"   Twitter: {len(startup['social_links']['twitter'])}")
        
        print("="*60)

def main():
    print("Y Combinator Startup Scraper")
    print("="*60)
    
    scraper = YCStartupScraper()
    
    # Scrape companies (limit to 50 for reasonable execution time)
    # You can adjust the limit or add batch filters
    scraper.scrape_companies_list(limit=50)
    
    # Save results
    scraper.save_to_json('yc_startups.json')
    scraper.save_to_csv('yc_startups.csv')
    
    # Print summary
    scraper.print_summary()
    
    print("\n✓ Scraping completed successfully!")
    print("Output files: yc_startups.json, yc_startups.csv")

if __name__ == "__main__":
    main()
