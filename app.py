import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.climatempo.com.br/').text

soup = BeautifulSoup(html, 'html.parser')

# tempMin = soup.find(id='min-temp-1')
# print(tempMin.text)

tempMax = soup.find(id='max-temp-1')
print(tempMax.text)