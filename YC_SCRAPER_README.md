# 🚀 Y Combinator Startup Scraper

A complete Python solution for scraping and analyzing Y Combinator startup data.

## ✨ What This Does

Extracts comprehensive information about recently funded Y Combinator startups:
- **Company details**: Name, description, batch, website
- **Founder information**: Names and roles
- **Social media**: LinkedIn, Twitter, GitHub profiles
- **Structured output**: JSON and CSV formats

## 📦 What's Included

### Core Scripts
1. **yc_scraper_stdlib.py** - Ready to run, no dependencies (uses sample data)
2. **yc_scraper.py** - Full web scraper (requires: requests, beautifulsoup4)
3. **example_analysis.py** - Data analysis examples

### Documentation
4. **README_SCRAPER.md** - Detailed technical documentation
5. **USAGE_GUIDE.md** - Quick start and examples
6. **PROJECT_SUMMARY.md** - Complete project overview
7. **requirements.txt** - Python dependencies

### Output Files (Generated)
8. **yc_startups.json** - Structured JSON data
9. **yc_startups.csv** - Spreadsheet format
10. **yc_founders_list.csv** - Extracted founder list

## 🎯 Quick Start

### Option 1: Run Immediately (No Setup)
```bash
python3 yc_scraper_stdlib.py
```
This generates sample data from 10 recent YC startups.

### Option 2: Full Web Scraping
```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper
python3 yc_scraper.py
```

### Option 3: Analyze Existing Data
```bash
python3 example_analysis.py
```

## 📊 Sample Output

### JSON Format
```json
{
  "company_name": "Vapi",
  "description": "Voice AI platform for developers...",
  "batch": "W24",
  "product_link": "https://vapi.ai",
  "founders": [{"name": "Nikhil Gupta", "role": "Founder"}],
  "social_links": {
    "linkedin": ["https://linkedin.com/in/nikhil-gupta"],
    "twitter": ["https://twitter.com/vapi"],
    "github": ["https://github.com/vapi"]
  }
}
```

### CSV Format
| company_name | batch | product_link | founders_names | linkedin_profiles |
|--------------|-------|--------------|----------------|-------------------|
| Vapi | W24 | https://vapi.ai | Nikhil Gupta | https://linkedin.com/in/nikhil-gupta |

## 🎨 Features

✅ **Two Versions**: Standard library (no deps) and full scraper  
✅ **Multiple Formats**: JSON and CSV output  
✅ **Complete Data**: Company, founders, social media  
✅ **Analysis Tools**: Example scripts included  
✅ **Well Documented**: Comprehensive guides  
✅ **Production Ready**: Error handling, rate limiting  

## 📈 Sample Companies Included

- **Vapi** (W24) - Voice AI platform
- **Basepilot** (W24) - AI customer support
- **Trieve** (W24) - Search infrastructure
- **Hyperbound** (S23) - AI sales training
- **Reworkd** (S23) - AI web automation
- **Mintlify** (S21) - Documentation
- **Supabase** (S20) - Firebase alternative
- **Retool** (W17) - Internal tools
- **Vercel** (S15) - Frontend platform
- **Anthropic** (S21) - AI safety

## 💡 Use Cases

1. **Market Research** - Analyze YC startup trends
2. **Competitor Analysis** - Track companies in your space
3. **Investor Research** - Find investment opportunities
4. **Networking** - Connect with founders
5. **Data Analysis** - Export to Excel/Sheets

## 🔧 Customization

### Change Number of Companies
```python
scraper.scrape_yc_api(limit=100)  # Scrape 100 companies
```

### Filter by Batch
```python
scraper.scrape_companies_list(batch_filter='W24', limit=50)
```

## 📚 Documentation

- **README_SCRAPER.md** - Full technical documentation
- **USAGE_GUIDE.md** - Quick start guide with examples
- **PROJECT_SUMMARY.md** - Complete project overview

## 🎓 Example Analysis

The `example_analysis.py` script demonstrates:
- Batch distribution analysis
- Founder statistics
- Social media presence metrics
- Exporting founder lists
- Data visualization examples

Run it with:
```bash
python3 example_analysis.py
```

## 📊 Data Statistics

From the sample dataset:
- **10 companies** across 6 YC batches
- **16 founders** total (avg 1.6 per company)
- **100% LinkedIn** coverage
- **50% Twitter** presence
- **40% GitHub** profiles

## ⚠️ Important Notes

1. **Sample Data**: stdlib version uses curated sample data
2. **Rate Limiting**: Full scraper includes respectful delays
3. **Terms of Service**: Respect YC's ToS when scraping
4. **Data Accuracy**: Verify critical information from sources
5. **Ethical Use**: Use data responsibly

## 🐛 Troubleshooting

### Missing Dependencies
```bash
pip install requests beautifulsoup4 lxml
```

### No Output Files
Run the scraper first:
```bash
python3 yc_scraper_stdlib.py
```

### Python Version
Requires Python 3.6 or higher:
```bash
python3 --version
```

## 📞 Support

1. Check **USAGE_GUIDE.md** for examples
2. Review **README_SCRAPER.md** for details
3. Examine code comments in Python files

## 📄 License

MIT License - Free to use and modify

## 🎉 Success!

All files are ready to use. Start with:
```bash
python3 yc_scraper_stdlib.py
```

Then explore the generated JSON and CSV files!

---

**Made with ❤️ for YC startup research**
