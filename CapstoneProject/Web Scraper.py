# imports Python libraries for use
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# defines which browser we are using for the webscraper
driver = webdriver.Chrome()

#insert urls you wish to visit
urls = ['http://vkr.e2a.mytemp.website/', 'http://vkr.e2a.mytemp.website/page2.html', 'http://vkr.e2a.mytemp.website/page3.html','http://vkr.e2a.mytemp.website/page4.html']

# pulls up desired url that is inputted into code to scrape
for item in urls:
    driver.get(item)

# Object "results" is an empty set used to store our scraped data
    results = []
    other_results = []
    # Add the page source to the variable 'content'
    # Loads the contents of the page into BeautifulSoup
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    for a in soup.find_all(attrs={'class': 'post'}):
        name = a.find('h2')
        if name not in results:
            results.append(name.text)
    for b in soup.find_all(attrs={'class': 'post'}):
        name2 = b.find('button')
        if name2 not in other_results:
            other_results.append(name2.text)

    series1 = pd.Series(results, name='Names')
    series2 = pd.Series(other_results, name='Prices')
    df = pd.DataFrame({'Names': results, 'Prices': other_results})
    df.to_csv('products.csv', index=False, encoding='utf-8')


