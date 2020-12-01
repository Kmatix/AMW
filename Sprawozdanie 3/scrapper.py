import requests
from bs4 import BeautifulSoup


result = requests.get("https://lowcygier.pl/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

newest_post = soup.find('h2', class_='post-title')
for a in newest_post.find_all('a', href=True):
    table = [a['href']]
    print(table[0])

input()

