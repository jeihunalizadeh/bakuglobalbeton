# Y Combinator Startup Scraper - Usage Guide

## 📋 Overview

This project contains Python scripts to scrape Y Combinator startup information including:
- Company name and description
- Product/website links
- Batch information (funding round)
- Founders' names
- Social media profiles (LinkedIn, Twitter, GitHub)

## 🚀 Quick Start

### Option 1: Standard Library Version (No Dependencies)

This version works out of the box with Python 3 and includes sample data:

```bash
python3 yc_scraper_stdlib.py
```

**Output:**
- `yc_startups.json` - Detailed JSON format
- `yc_startups.csv` - Spreadsheet-friendly format

### Option 2: Full Scraper (Requires Dependencies)

For actual web scraping from YC's website:

1. Install dependencies:
```bash
pip install requests beautifulsoup4 lxml
```

2. Run the scraper:
```bash
python3 yc_scraper.py
```

## 📊 Output Format

### JSON Structure
```json
{
  "company_name": "Vapi",
  "description": "Voice AI platform for developers...",
  "batch": "W24",
  "company_url": "https://www.ycombinator.com/companies/vapi",
  "product_link": "https://vapi.ai",
  "founders": [
    {
      "name": "Nikhil Gupta",
      "role": "Founder"
    }
  ],
  "social_links": {
    "linkedin": ["https://linkedin.com/in/nikhil-gupta"],
    "twitter": ["https://twitter.com/vapi"],
    "github": ["https://github.com/vapi"]
  },
  "scraped_at": "2025-11-04T15:24:22.574028"
}
```

### CSV Columns
- `company_name` - Name of the startup
- `description` - What the company does
- `batch` - YC batch (e.g., W24, S23)
- `company_url` - YC profile page
- `product_link` - Company website
- `founders_names` - Semicolon-separated list
- `linkedin_profiles` - Semicolon-separated LinkedIn URLs
- `twitter_profiles` - Semicolon-separated Twitter URLs
- `github_profiles` - Semicolon-separated GitHub URLs
- `scraped_at` - Timestamp of scraping

## 📁 Files Included

1. **yc_scraper_stdlib.py** - Standard library version (no dependencies)
2. **yc_scraper.py** - Full-featured scraper (requires dependencies)
3. **requirements.txt** - Python package dependencies
4. **README_SCRAPER.md** - Detailed documentation
5. **USAGE_GUIDE.md** - This file

## 🔍 Sample Data

The standard library version includes sample data from recent YC batches:
- **W24 (Winter 2024)**: Vapi, Basepilot, Trieve
- **S23 (Summer 2023)**: Hyperbound, Reworkd
- **S21 (Summer 2021)**: Mintlify, Anthropic
- **S20 (Summer 2020)**: Supabase
- **W17 (Winter 2017)**: Retool
- **S15 (Summer 2015)**: Vercel

## 💡 Use Cases

1. **Market Research**: Analyze trends in YC-funded startups
2. **Competitor Analysis**: Track companies in your space
3. **Investor Research**: Identify promising startups
4. **Networking**: Find founders to connect with
5. **Data Analysis**: Export to Excel/Google Sheets for analysis

## 🛠️ Customization

### Change Number of Companies
Edit the script and modify the `limit` parameter:

```python
scraper.scrape_yc_api(limit=50)  # Scrape 50 companies
```

### Filter by Batch
For the full scraper version:

```python
scraper.scrape_companies_list(batch_filter='W24', limit=50)
```

## 📈 Analyzing the Data

### Using Python
```python
import json
import pandas as pd

# Load JSON
with open('yc_startups.json', 'r') as f:
    data = json.load(f)

# Load CSV
df = pd.read_csv('yc_startups.csv')

# Analysis examples
print(f"Total companies: {len(df)}")
print(f"Batches: {df['batch'].value_counts()}")
print(f"Companies with LinkedIn: {df['linkedin_profiles'].notna().sum()}")
```

### Using Excel/Google Sheets
1. Open `yc_startups.csv` in Excel or Google Sheets
2. Use filters and pivot tables for analysis
3. Create charts to visualize trends

## ⚠️ Important Notes

1. **Rate Limiting**: The scraper includes delays to be respectful to YC's servers
2. **Sample Data**: The stdlib version uses sample data for demonstration
3. **Data Accuracy**: Always verify critical information from official sources
4. **Terms of Service**: Respect Y Combinator's terms of service
5. **Ethical Use**: Use scraped data responsibly and ethically

## 🐛 Troubleshooting

### "No module named 'requests'"
Install dependencies:
```bash
pip install requests beautifulsoup4 lxml
```

Or use the standard library version:
```bash
python3 yc_scraper_stdlib.py
```

### Empty Output Files
Check your internet connection and ensure the script completed successfully.

### Missing Social Links
Not all companies have public social media links. This is expected.

## 📞 Support

For issues or questions:
1. Check the README_SCRAPER.md for detailed documentation
2. Review the code comments in the Python files
3. Ensure you're using Python 3.6 or higher

## 📄 License

MIT License - Free to use and modify for your needs.

---

**Happy Scraping! 🚀**
