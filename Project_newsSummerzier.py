import requests
from bs4 import BeautifulSoup
import nltk


# Create a header
headers = {'User-Agent': 'Mozilla/5.0'}

# Request the webpage
requests = requests.get('https://www.bbc.com/news',headers=headers)
html = requests.content

# create some soup
soup = BeautifulSoup(html,'html.parser')

# Uses to easily read the html that we scrapered
# print(soup.prettify())

def bbc_news_scraper(keyword):
    news_list = []

    # Find all the headers in BBC Home
    for h in soup.find_all('h3',class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'):
        news_title =  h.contents[0].lower()  

        if news_title not in news_list:
            if 'bbc' not in news_title:
                news_list.append(news_title)

    no_of_news =0
    keyword_list = []
    # Goes through the list and search keyword
    for i , title in enumerate(news_list):
        text = ''
        if keyword.lower() in title:
            text = ' <----------------------- KEYWORD'
            no_of_news += 1
            keyword_list.append(title)
        print(i+1, ':' , title , text)

        # print the title of the article that contain keyword
        print(f'\n --------------- Total mentions of = "{keyword}" = {no_of_news} ------------')

        for i , title in enumerate(keyword_list):
            print(i+1,':',title)

bbc_news_scraper('World')                