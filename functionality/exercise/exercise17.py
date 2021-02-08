import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text)


