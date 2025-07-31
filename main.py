import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
print(response.content)

import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the website
url = 'https://www.bbc.com/news'
response = requests.get(url)
html = response.content

# Step 2: Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Extract headlines
# BBC's headlines are often in <h3> or <h2> tags with specific classes
headlines = soup.find_all(['h3', "img" , 'h2'])

print("\n🔹 Latest BBC News Headlines:\n")
for i, headline in enumerate(headlines[:10], 1):  # Get top 10 only
    text = headline.get_text(strip=True)
    if text:
        print(f"{i}. {text}")
        
import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <img> tags
images = soup.find_all('img')

print("\n🖼️ BBC News Images Found:\n")
for i, img in enumerate(images[:10], 1):  # Just first 10 for demo
    src = img.get('src') or img.get('data-src')
    if src and src.startswith('http'):
        print(f"{i}. {src}")        
        