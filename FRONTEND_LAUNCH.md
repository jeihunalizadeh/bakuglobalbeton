# 🚀 Frontend Launch Guide

## Quick Start - View Your Website

### Option 1: Using Python Script (Recommended)
```bash
python3 launch_frontend.py
```
This will automatically open the website in your default browser.

### Option 2: Direct File Access
Simply open this file in any web browser:
```
/vercel/sandbox/src/index.html
```

You can:
- Double-click the file in your file manager
- Drag and drop it into a browser window
- Right-click and select "Open with Browser"

### Option 3: Using Command Line
```bash
# On Linux with xdg-open
xdg-open /vercel/sandbox/src/index.html

# On macOS
open /vercel/sandbox/src/index.html

# On Windows
start /vercel/sandbox/src/index.html
```

## 📁 Website Structure

Your website includes:
- **Home Page**: `src/index.html` (Main landing page)
- **About**: `src/about.html` (Company information)
- **Services**: `src/servis.html` (Services offered)
- **Projects**: `src/projects.html` (Project portfolio)
- **Products**: `src/products.html` (Product catalog)
- **Contact**: `src/contact.html` (Contact information)

## 🎨 Features

- Responsive Bootstrap design
- Image carousel/slider
- Interactive navigation
- Google Maps integration
- FontAwesome icons
- Mobile-friendly layout

## 📝 Notes

- This is a static HTML website (no server required!)
- All pages can be viewed directly in your browser
- External resources (Bootstrap, FontAwesome) are loaded from CDN
- Some features may require internet connection for external resources

## 🔧 Troubleshooting

**Images not showing?**
- Check that the `src/images/` directory contains all required images
- Verify image paths in HTML files

**Styles not loading?**
- Check that `src/css/style.css` exists
- Ensure internet connection for Bootstrap/FontAwesome CDN

**JavaScript not working?**
- Check that `src/js/script.js` exists
- Ensure jQuery is loading from CDN

---

**Website**: Baku Global Beton
**Language**: Azerbaijani (Az)
**Framework**: Bootstrap 4 + jQuery
