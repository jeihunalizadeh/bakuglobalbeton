#!/usr/bin/env python3
"""
Frontend Launcher Script
This script helps you view the frontend by opening it in your default browser.
"""

import os
import webbrowser
from pathlib import Path

def launch_frontend():
    """Launch the frontend in the default browser"""
    # Get the absolute path to index.html
    current_dir = Path(__file__).parent
    index_path = current_dir / "src" / "index.html"
    
    if not index_path.exists():
        print(f"❌ Error: index.html not found at {index_path}")
        return False
    
    # Convert to file:// URL
    file_url = f"file://{index_path.resolve()}"
    
    print("🚀 Launching frontend...")
    print(f"📂 Opening: {file_url}")
    print("\n" + "="*60)
    print("Frontend is now opening in your default browser!")
    print("="*60)
    print(f"\nIf it doesn't open automatically, copy this URL:")
    print(f"  {file_url}")
    print("\nOr navigate to this file in your browser:")
    print(f"  {index_path.resolve()}")
    print("="*60)
    
    # Open in default browser
    try:
        webbrowser.open(file_url)
        return True
    except Exception as e:
        print(f"⚠️  Could not automatically open browser: {e}")
        print(f"Please manually open: {file_url}")
        return False

if __name__ == "__main__":
    launch_frontend()
