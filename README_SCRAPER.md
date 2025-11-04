# Y Combinator Startup Scraper

A Python web scraper that extracts information about recently funded Y Combinator startups.

## Features

The scraper extracts the following information for each startup:
- **Company Name**: The name of the startup
- **Description**: Brief description of what the company does
- **Batch**: YC batch information (e.g., W24, S23)
- **Product Link**: Link to the company's website/product
- **Founders**: Names and roles of founders
- **Social Media**: LinkedIn, Twitter/X, and GitHub profiles of founders

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install requests beautifulsoup4 pandas lxml
```

## Usage

### Basic Usage

Run the scraper with default settings (scrapes 50 companies):
```bash
python yc_scraper.py
```

### Output Files

The scraper generates two output files:

1. **yc_startups.json** - Detailed JSON format with nested structure
2. **yc_startups.csv** - Flat CSV format for easy analysis in Excel/Google Sheets

### Customization

You can modify the scraper by editing `yc_scraper.py`:

```python
# Change the number of companies to scrape
scraper.scrape_companies_list(limit=100)  # Scrape 100 companies

# Filter by specific batch
scraper.scrape_companies_list(batch_filter='W24', limit=50)
```

## Output Format

### JSON Structure
```json
{
  "company_name": "Example Startup",
  "description": "Building the future of...",
  "batch": "W24",
  "company_url": "https://www.ycombinator.com/companies/example",
  "product_link": "https://example.com",
  "founders": [
    {
      "name": "John Doe",
      "role": "Founder"
    }
  ],
  "social_links": {
    "linkedin": ["https://linkedin.com/in/johndoe"],
    "twitter": ["https://twitter.com/johndoe"],
    "github": ["https://github.com/johndoe"]
  },
  "scraped_at": "2024-11-04T12:00:00"
}
```

### CSV Columns
- company_name
- description
- batch
- company_url
- product_link
- founders_names (semicolon-separated)
- linkedin_profiles (semicolon-separated)
- twitter_profiles (semicolon-separated)
- github_profiles (semicolon-separated)
- scraped_at

## Rate Limiting

The scraper includes built-in rate limiting (1 second delay between requests) to be respectful to YC's servers. Please do not modify this to scrape faster.

## Notes

- The scraper respects robots.txt and includes appropriate delays
- Some companies may not have all information available
- Social media links are extracted from company pages when available
- The scraper uses a reasonable User-Agent header

## Troubleshooting

### Connection Errors
If you encounter connection errors, the scraper will automatically retry up to 3 times.

### Missing Data
Not all companies have complete information. The scraper will extract whatever is available.

### Rate Limiting
If you're being rate-limited, increase the delay in the `scrape_company_details` method.

## Legal & Ethical Considerations

- This scraper is for educational and research purposes
- Respect Y Combinator's terms of service
- Do not use scraped data for spam or unauthorized commercial purposes
- Always verify data accuracy before using it

## License

MIT License - Feel free to modify and use as needed.
