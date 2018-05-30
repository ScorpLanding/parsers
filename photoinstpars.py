from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = 'https://instagram.com/'+input('Username of profile: ')
links = []
wens = webdriver.Firefox()
try:
    wens.get(url)
    a = wens.find_element_by_css_selector('div._6d3hm:nth-child(1)')
    a.click()
    html = wens.page_source
    wens.close()
except:
    wens.close()
time.sleep(1)
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('div', class_='_mck9w _gvoze _tn0ps'):
    link_get = link.find('a')
    append_method = link_get.get('href')
    links.append(url[:25]+append_method)
for n in range(len(links)):
    r = requests.get(links[n]).content
    soups = BeautifulSoup(r, 'html.parser')
    for img in soups.select('meta:nth-of-type(11)'):
        print(img)
        link_photo = img.get('content')
        img_d = requests.get(link_photo).content
        open(link_photo[127:], 'wb').write(img_d)
        print(link_photo[127:])
