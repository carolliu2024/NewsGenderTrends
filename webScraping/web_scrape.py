# This script is not finished yet. 
# Idea: not every news site has a (free) API that can be used to access all of their articles, so we try to use web scraping to get the articles.
# I wanted to try using Flask to connect the backend, and use Selenium so that I could "click" the article links and get their content (not implemented yet)
# Below, I try to scrape the headings of 3 randomly sampled articles (CNN) from each month in the date specified by the 
# user (month/year only; day can be implemented later).
# Instead of trying to get the content of every single article, I wanted to get a random sample of at least 30 (bc statistics)
# over the entire date span so that it would be representative of the articles.
# Once we get the article content, we can analyze it for gender bias.



# %%
# BeautifulSoup package: parses HTML of URL, accesses elts
# through tags and attributes
# %pip install beautifulsoup4
# lxml: HTML parser for BeautifulSoup; note: doesn't work, just use default for python
# %pip install lxml
# requests module: get HTML code from page
# %pip install requests

# %% Imports
import requests
from bs4 import BeautifulSoup
from datetime import date
import random

# %%
today = date.today()
# print(today)
# d = today.strftime("%m-%d-%y")
year_start = 2019
month_start = 3
year_end = 2020
month_end = 1

# If given the month number (e.g. month 2, month 20 since the start date)
# return the month number, e.g. 1 through 12 (Jan - Dec)
def month_num(x):
    month = (3+x)%12
    return month if month!=0 else 12

i = 0
switch_to_next_yr = False # Flag for while loop below to indicate when to increment to the next year
months = (year_end - year_start) * 12 + month_end - month_start # Number of months within the dates specified

for year in range(year_start,year_end+1):
    print("year = ", year)
    switch_to_next_yr = False
    while (i <= months) and not switch_to_next_yr:
        month = month_num(i)
        cnn_url = "https://www.cnn.com/article/sitemap-{}-{}.html".format(year, month)
        # cnn_url="https://edition.cnn.com/world/live-news/coronavirus-pandemic-{}-intl/index.html".format(d)
        html = requests.get(cnn_url)
        bsobj = BeautifulSoup(html.content,'html.parser') # BeautifulSoup object
        # Randomly sample 3 articles on page
        articles = bsobj.findAll("span", class_="sitemap-link")[1:]
        num_articles = len(articles)
        if num_articles <= 3:
            articles3 = random.sample(articles, num_articles)
        else:
            articles3 = random.sample(articles, 3)
        
        for link in articles3:
            # print( "Headline : {}".format(link.text))
            print("YEAR: ",year, " MONTH:", month)
        i += 1
        # If month switched from 12 to 1, increase year
        if month == 12 and month_num(i) == 1:
            switch_to_next_yr = True

# %%
