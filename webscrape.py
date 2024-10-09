# Quotes web scraping project, this project has the objetive of generate an interactive table table
# that has a list of quotes with their respective authors, using MySQL Workbench and some other resources 
# that will be defined as the project takes shape. I would like to add a filter, search and "add to favorites" 
# option in my interactive table. I need to pull the data from Goodreads, then insert it into MySQL Workbench, pull 
# pull the data from MySQL so i can create the table, "add to favorites" option and finally the filter options. 

# Start date: 1/10/2024 (dd/mm/yyyy)

#-------------------------------------------------------------------------------------------------------------------------------------

#Libraries 


# importing required libraries
import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
import re

#from IPython.display import display, Image

#Defining the url and the response to the request

# https://quotes.toscrape.com/page/1/


#Retrieve Quotes
def scrape_data(): 
    try: 
        quotes_list = []

        authors = set()

        for page in range(11):
        
            base_url = f'https://quotes.toscrape.com/page/'
            url = f'{base_url}{page}/'


            response = requests.get(url) 

            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the desired data (modify according to the website's structure)
            for item in soup.find_all('div', class_='quote'):  # Adjust the selector as needed
                quote = item.find('span', class_ = 'text').text  # Example: extracting the title
                author = item.find('small', class_ = 'author').text
                
                # Append the quote as a dictionary to the list
                quotes_list.append((quote, author, 0)) #0 is default for favourite

                authors.add(author)

                
        unique_authors = list(authors)


    except: 
        print("Error retrieving quotes")

    try:
        #Extract information for each individual author, in JSON form. 
        #name, birth, description
        # Function to format the author URL
        def format_author_url(author_name):
            # Replace dots and spaces with hyphens, and remove apostrophes
            formatted_name = author_name.replace('.', '-')  # Replace dots with hyphens
            formatted_name = formatted_name.replace(" ", "-")  # Replace spaces with hyphens
            formatted_name = formatted_name.replace("'", "")  # Remove apostrophes
            formatted_name = formatted_name.replace('--', '-') #Remove double --
            return f"https://quotes.toscrape.com/author/{formatted_name}/"

        authors_urls = []

        for author in unique_authors:
            author_url = format_author_url(author)
            authors_urls.append(author_url)

        #Data for the authors

        authors_data = []

        for url in authors_urls:
            response = requests.get(url) 
            soup = BeautifulSoup(response.text, 'html.parser')

            #Extract the desired data
            for item in soup.find_all('div', class_='author-details'): #div element with class=authors-details
                author = item.find('h3', class_ = 'author-title').text  # Example: extracting the title
                birth_date = item.find('span', class_ = 'author-born-date').text
                birth_loc = item.find('span', class_ = 'author-born-location').text
                description = item.find('div', class_='author-description').text
                

            if author == '':
                pass
            else: 
                authors_data.append((author, birth_date, birth_loc, description))
        
    except: 
        return("Error retrieving authors information")
    
    return authors_data, quotes_list

if __name__ == "__main__":
    data = scrape_data()



