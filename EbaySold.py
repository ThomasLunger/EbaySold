import requests
from bs4 import BeautifulSoup

def get_latest_sold_listings():
    keyword = input('Enter a Product/Keyword to Begin:')
    url = f"https://www.ebay.com/sch/i.html?_nkw={keyword}&LH_Sold=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    listings = soup.find_all('li', {'class': 's-item s-item__pl-on-bottom'})
    for listing in listings:
        title_elem = listing.find('span', {'role': 'heading'}).get_text()
        price_elem = listing.find('span', {'class': 's-item__price'}).get_text()
        date_elem = listing.find('span', {'class': 'POSITIVE'})
        if date_elem != None:
            date_elem = str(date_elem)
            date_elem = date_elem.replace('<span class="POSITIVE">','')
            date_elem = date_elem.replace('</span>','')
        else:
            continue
        print('|')
        print(title_elem)
        print(price_elem)
        print(date_elem)

def __main__():
    print('Ebay Sold Items Viewer - Made by Thomas Lunger on GitHub!')
    print('PRESS CTRL-C TO STOP THE SCRIPT')
    while True:
        get_latest_sold_listings()
__main__()
