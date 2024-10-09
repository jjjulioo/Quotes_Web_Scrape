from webscrape import scrape_data
from database import insert_data
import mysql.connector

# Scrape the data
try:
    authors_data, quotes_list = scrape_data()
except Exception as e:
    print(f"An error occurred scraping the data: {e}")

# Insert the data into the database
try:
    data_insert = insert_data(authors_data, quotes_list)
    print(data_insert)
except Exception as e:
    print(f'An error occurred inserting the data: {e}')





