import unittest
import os
import json
import sys

# Add the parent directory to the sys.path to handle the import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from web_scraping_script import scrape_books

class TestWebScraping(unittest.TestCase):
    def test_scrape_books(self):
        """
        Test the scrape_books function.
        """
        # Run the scrape_books function
        scrape_books()

        # Check if the JSON file is created
        self.assertTrue(os.path.exists('data/scraped_books.json'))

        # Check if the JSON file is not empty
        with open('data/scraped_books.json', 'r') as file:
            data = json.load(file)
            self.assertTrue(len(data) > 0)

if __name__ == '__main__':
    unittest.main()
