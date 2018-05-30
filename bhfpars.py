import cfscrape
from bs4 import BeautifulSoup
import csv

print('######################################')
print('# Black Hat Forum Parser by ScorpDEv #')
print('######################################')

url = 'https://bhf.io/'
urls_wr = []
wr_l = []

scrape = cfscrape.create_scraper()
html = scrape.get(url).content
soup = BeautifulSoup(html, 'html.parser')
print('Get Sections')
for th_klass in soup.find_all('h3', class_='node-title'):
    th_link = th_klass.find('a').get('href')
    urls_wr.append(url[:14]+th_link)
print('Successful, get Threads')
for nmb in range(0, len(urls_wr)):
    html_wr = scrape.get(urls_wr[nmb]).content
    soup_wr = BeautifulSoup(html_wr, 'html.parser')
    for wr_klass in soup_wr.find_all('div', class_='structItem-title'):
        wr_link = wr_klass.find('a').get('href')
        wr_l.append(url[:14]+wr_link)
print('Successful, get content and writing to CSV File')
for nmb_wr in range(0, len(wr_l)):
    html_thr = scrape.get(wr_l[nmb_wr]).content
    soup_thr = BeautifulSoup(html_thr, 'html.parser')
    text_thr = soup_thr.find('div', class_='bbWrapper').text
    title_thr = soup_thr.find('h1', class_='p-title-value').text
    ts_thr = soup_thr.find('a', class_='username').text
    data_thr = {'Thread': title_thr,
                    'Url': wr_l[nmb_wr],
                    'Username': ts_thr,
                    'Text': text_thr}
    with open('bhf.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow( (data_thr['Thread'],
                              data_thr['Url'],
                              data_thr['Username'],
                              data_thr['Text']) )
print('Successful!')

