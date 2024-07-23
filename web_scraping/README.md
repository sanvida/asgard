# Web Scraping Project

## Overview

This project demonstrates web scraping using Python. The script scrapes product data from the "Books to Scrape" website and saves it to a JSON file.

## Requirements

- Python 3.x
- requests
- beautifulsoup4

## Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd web_scraping

   ```

2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
   pip install -r requirements.txt

## Usage

Run the web scraping script:
python web_scraping_script.py

## Testing

Run the tests using unittest:
python -m unittest discover -s tests
