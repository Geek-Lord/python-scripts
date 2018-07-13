#! python3
# simple script for googling stuff from command line

import requests
import sys
import webbrowser
import bs4
if len(sys.argv) < 2:
    print("""Usage:

        python search <search term>""")
    exit()
print('Googling...')
res = requests.get(
    'http://www.google.co.in/search?q=' + ' '.join(sys.argv[1:])
)
soup = bs4.BeautifulSoup(res.text)
links = soup.select('.r a')
for i in range(0, 5):
    webbrowser.open(
        'http://google.com' + links[i].get('href'), new=0, autoraise=True)
