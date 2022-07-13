from bs4 import BeautifulSoup
import requests

url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"

result = requests.get(url)
print(result.text)