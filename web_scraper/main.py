import requests 
from bs4 import BeautifulSoup
import inflection


URL = 'http://www.dailysmarty.com/topics/python'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_="post-link-title")

for post in results:
    link = post.find('a')['href']
    part = link.partition('/')[2]
    print(inflection.titleize(part.partition('/')[2]))
    



