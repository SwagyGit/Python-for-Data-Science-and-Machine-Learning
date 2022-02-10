### Importing necessary packages ###
import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk

### Transferring data from excel file to dataframe ###
data_frame = pd.read_excel('Input.xlsx')

### Reading data from dataframe ###
for i in range(0,len(data_frame)-1):

	# Retriving url and url_id from series
    source_url = data_frame['URL'][i]
    text_file_name = data_frame['URL_ID'][i]

    # Adding a user agent to access the page information
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
    }

    # With request library grabbing the page
    source_page = requests.get(source_url, headers = headers)

    # Creating BeautifulSoup object to analyse the extracted page
    source_text = BeautifulSoup(source_page.text,"lxml")
    
    # Using select method we are grabbing our desired tags
    article_title_set = source_text.select('h1.entry-title')
    article_text_set = source_text.select('div.td-post-content')


    # Grabbing content from the tags
    article_title = article_title_set[0].getText()
    article_text = article_text_set[0].getText()

    # Creating a text file
    # File name is according to URL_ID    
    with open(str(text_file_name)+'.txt',"w+",encoding="utf-8") as text_file:

    	# Wrting on the file with scrapped data
        text_file.write(article_title+'\n'+article_text)

### END ###
