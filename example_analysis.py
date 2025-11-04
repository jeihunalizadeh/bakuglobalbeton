#!/usr/bin/env python3
"""
Example: How to analyze the scraped YC startup data
"""

import json
import csv
from collections import Counter

def analyze_json_data():
    """Analyze data from JSON file"""
    print("="*70)
    print("ANALYZING YC STARTUP DATA FROM JSON")
    print("="*70)
    print()
    
    # Load JSON data
    with open('yc_startups.json', 'r') as f:
        startups = json.load(f)
    
    print(f"📊 Total Startups: {len(startups)}")
    print()
    
    # Analyze batches
    batches = [s['batch'] for s in startups if s['batch']]
    batch_counts = Counter(batches)
    print("📅 Startups by Batch:")
    for batch, count in sorted(batch_counts.items(), reverse=True):
        print(f"   {batch}: {count} companies")
    print()
    
    # Analyze founders
    total_founders = sum(len(s['founders']) for s in startups)
    avg_founders = total_founders / len(startups) if startups else 0
    print(f"👥 Founder Statistics:")
    print(f"   Total founders: {total_founders}")
    print(f"   Average per company: {avg_founders:.1f}")
    print()
    
    # Analyze social media presence
    linkedin_count = sum(1 for s in startups if s['social_links']['linkedin'])
    twitter_count = sum(1 for s in startups if s['social_links']['twitter'])
    github_count = sum(1 for s in startups if s['social_links']['github'])
    
    print("🔗 Social Media Presence:")
    print(f"   LinkedIn: {linkedin_count}/{len(startups)} ({linkedin_count/len(startups)*100:.0f}%)")
    print(f"   Twitter:  {twitter_count}/{len(startups)} ({twitter_count/len(startups)*100:.0f}%)")
    print(f"   GitHub:   {github_count}/{len(startups)} ({github_count/len(startups)*100:.0f}%)")
    print()
    
    # Show top companies by description length (proxy for detail)
    print("📝 Most Detailed Descriptions:")
    sorted_by_desc = sorted(startups, key=lambda x: len(x['description']), reverse=True)[:3]
    for i, startup in enumerate(sorted_by_desc, 1):
        print(f"   {i}. {startup['company_name']}")
        print(f"      {startup['description'][:80]}...")
    print()
    
    # List all companies with their key info
    print("📋 Complete Company List:")
    print("-"*70)
    for i, startup in enumerate(startups, 1):
        founders_str = ', '.join([f['name'] for f in startup['founders']])
        print(f"{i:2d}. {startup['company_name']} ({startup['batch']})")
        print(f"    Founders: {founders_str}")
        print(f"    Website: {startup['product_link']}")
        print(f"    LinkedIn: {len(startup['social_links']['linkedin'])} profiles")
        print()
    
    print("="*70)

def analyze_csv_data():
    """Analyze data from CSV file"""
    print()
    print("="*70)
    print("ANALYZING YC STARTUP DATA FROM CSV")
    print("="*70)
    print()
    
    # Load CSV data
    with open('yc_startups.csv', 'r') as f:
        reader = csv.DictReader(f)
        startups = list(reader)
    
    print(f"📊 Total Startups: {len(startups)}")
    print()
    
    # Find companies with most founders
    print("👥 Companies with Most Founders:")
    sorted_by_founders = sorted(startups, 
                                key=lambda x: len(x['founders_names'].split(';')) if x['founders_names'] else 0, 
                                reverse=True)[:5]
    for i, startup in enumerate(sorted_by_founders, 1):
        founder_count = len(startup['founders_names'].split(';')) if startup['founders_names'] else 0
        print(f"   {i}. {startup['company_name']}: {founder_count} founders")
        if startup['founders_names']:
            print(f"      {startup['founders_names']}")
    print()
    
    # Find companies with most social links
    print("🔗 Companies with Most Social Links:")
    for startup in startups[:5]:
        linkedin = len(startup['linkedin_profiles'].split(';')) if startup['linkedin_profiles'] else 0
        twitter = len(startup['twitter_profiles'].split(';')) if startup['twitter_profiles'] else 0
        github = len(startup['github_profiles'].split(';')) if startup['github_profiles'] else 0
        total = linkedin + twitter + github
        if total > 0:
            print(f"   {startup['company_name']}: {total} links (L:{linkedin}, T:{twitter}, G:{github})")
    print()
    
    print("="*70)

def export_founder_list():
    """Export a simple list of all founders with their companies"""
    print()
    print("="*70)
    print("EXPORTING FOUNDER LIST")
    print("="*70)
    print()
    
    with open('yc_startups.json', 'r') as f:
        startups = json.load(f)
    
    founders_list = []
    for startup in startups:
        for founder in startup['founders']:
            founders_list.append({
                'founder_name': founder['name'],
                'company': startup['company_name'],
                'batch': startup['batch'],
                'website': startup['product_link']
            })
    
    # Save to CSV
    with open('yc_founders_list.csv', 'w', newline='') as f:
        fieldnames = ['founder_name', 'company', 'batch', 'website']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(founders_list)
    
    print(f"✓ Exported {len(founders_list)} founders to yc_founders_list.csv")
    print()
    print("Sample entries:")
    for founder in founders_list[:5]:
        print(f"   {founder['founder_name']} - {founder['company']} ({founder['batch']})")
    print()
    print("="*70)

def main():
    """Run all analysis examples"""
    try:
        analyze_json_data()
        analyze_csv_data()
        export_founder_list()
        
        print()
        print("✓ Analysis complete!")
        print()
        print("Generated files:")
        print("  - yc_founders_list.csv (list of all founders)")
        print()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please run yc_scraper_stdlib.py first to generate the data files.")
    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    main()
