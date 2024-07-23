# Web Scraping Project

## Overview

This project demonstrates web scraping using Python. The script scrapes product data from the "Books to Scrape" website and saves it to a JSON file.

## Requirements

- Python 3.6 or later
- requests
- beautifulsoup4

## Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/sanvida/asgard.git
   cd web_scrapping
   ```

2. **Create and Activate a Virtual Environment**

   I. Create a virtual environment

   ```python
   python -m venv venv
   ```

   II. Activate the virtual environment

   **On Windows**

   ```python
   venv\Scripts\activate
   ```
   
   **On macOS/Linux**
   ```sh
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Ensure you are in the virtual environment and install the required packages:
   ```python
   pip install -r requirements.txt
   ```

## Usage

Run the web scraping script:
```python
python web_scraping_script.py
```
After running the web scrapping script json data will be generated and stored inside the `data` folder.

## Testing

Run the tests using unittest:
```python
python -m unittest discover -s tests
```

## Using GitHub Codespaces

1. **Open in Codespaces**: Click the "Code" button on the GitHub repository page and select "Open with Codespaces" to create a new Codespace.
2. Change the directory
   ```bash
   cd web_scrapping
   ```
4. **Install Dependencies**: Once the Codespace is set up, run the following commands in the terminal to install the required dependencies:
   ```bash
   pip install -r requirements.txt
5. Run the web scraping script:
    ```python
   python web_scraping_script.py
   ```
   After running the web scrapping script json data will be generated and stored inside the `data` folder.

5. Testing
   Run the tests using unittest:
   ```python
   python -m unittest discover -s tests
   ```
