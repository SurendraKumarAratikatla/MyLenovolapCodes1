import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://www.indiabix.com/aptitude/clock/").read()
soup = bs.BeautifulSoup(source,'lxml')

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

#print(soup.get_text())

for url in soup.find_all('a'):
    print(url.get('href'))