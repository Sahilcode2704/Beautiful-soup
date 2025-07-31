import pandas as pd
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the website
url = 'https://www.youtube.com/'
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
        