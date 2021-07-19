import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

#df = pd.read_html('http://127.0.0.1:8000/admin/account/account/')

result_dict = {}
country_dict = {}
world_status_dict = {}
url = "http://127.0.0.1:8000/admin/account/account/"
# here headers providing for avoiding forbidden type of issues
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

response = requests.get(url, headers=headers)
# making soup to scrap data
soup = BeautifulSoup(response.content, 'html.parser')
# searching for pattern to march tabledata
soup = re.sub(r'<.*?>', lambda g: g.group(0).upper(), str(soup))
# creating dataframe by using read_html into df variable
df = pd.read_html(soup)