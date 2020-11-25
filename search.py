import urllib
import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.txt')
URL = (parser.get('Default', 'URL'))
USER_AGENT = (parser.get('Default', 'USER_AGENT'))
headers = {"user-agent": USER_AGENT}


# function to get page data
def get_page_data(soup):
    results = []
    for g in soup.find_all('div', class_='post-block-out'):
        print('--------------------')
        print(g.prettify())
        anchors = g.find_all('a', class_='preview')
        if anchors:
            link = anchors[0]['href']
            title = anchors[0]['title']
            image = anchors[0]['data-rel']
        post_price = g.find_all('p', class_='post-price')
        if post_price:
            price = post_price[0].next
        post_discription = g.find_all('p', class_='post-desc')
        if post_discription:
            description = post_discription[0].next
        post_city = g.find_all('div', class_='clr')
        if post_city:
            city = post_city[0].next
        post_category = g.find_all('a', class_='cp-fixed-color')
        if post_category:
            category = post_category[0].next
        post_person = g.find_all('a', rel_='author')
        if post_person :
            person = post_person[0].next
        item = {
            "title": title,
            "link": link,
            "image": image,
            "price": price.strip(),
            "description": description,
            "city": city.strip(),
            "category": category,
            "person": person
        }
        results.append(item)
    return results


# Main call
resp = requests.get(URL, headers=headers)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = get_page_data(soup)
    print(*results, sep='\n')
