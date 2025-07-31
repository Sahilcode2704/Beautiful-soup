import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
print(response.content)