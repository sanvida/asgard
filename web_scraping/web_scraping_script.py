import requests
from bs4 import BeautifulSoup
import json

def scrape_books():
    """
    Scrapes book data from the 'Books to Scrape' website and saves it to a JSON file.
    
    Returns:
        None
    """
    # Define the URL of the website to scrape
    url = 'http://books.toscrape.com/'

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the container that holds the product data
        product_container = soup.find_all('article', class_='product_pod')

        # Initialize a list to store the product data
        products = []

        # Loop through each product item and extract details
        for product in product_container:
            product_name = product.find('h3').find('a')['title']
            product_price = product.find('p', class_='price_color').text.strip()
            product_rating = product.find('p')['class'][1]  # Class names include rating, e.g., 'star-rating Three'

            # Create a dictionary for the product
            product_data = {
                'name': product_name,
                'price': product_price,
                'rating': product_rating
            }

            # Add the product data to the list
            products.append(product_data)

        # Convert the list of products to JSON format
        products_json = json.dumps(products, indent=4)

        # Save the scraped data to a JSON file
        with open('data/scraped_books.json', 'w') as file:
            file.write(products_json)

        print('Data successfully scraped and saved to data/scraped_books.json')

    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

if __name__ == '__main__':
    scrape_books()
