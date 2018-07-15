# script to search a movie from command line and print it's rating and description from imdb
import requests
from bs4 import BeautifulSoup
from sys import argv

search = 'https://www.imdb.com/find?q='
if len(argv) < 2:
    print(
        """Usage:

            imdb <search term>
        """
    )
    exit()
query = search + '+'.join(argv[1:])
print('Searching...')
res = requests.get(query)
soup = BeautifulSoup(res.text, 'lxml')
result = soup.find_all('td', class_='result_text')
sres = result[0].find_all('a')
for i in sres:
    link = (i['href'])
print('Getting movie details...')
page = requests.get('https://www.imdb.com' + link)
soup2 = BeautifulSoup(page.text, 'lxml')
mov_name = soup2.find('h1').text.replace('\xa0', ' ')
print('Details for movie:' + mov_name)
ratings = soup2.find_all('span', itemprop="ratingValue")
print('IMDb rating: ' + ratings[0].text)
desc = soup2.find('span', itemprop="description")
print('Description:\n' + desc.text)
