import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/1310/franciscobeltrao-pr').text

soup = BeautifulSoup(html, 'html.parser')


local = soup.find(class_="-bold -font-18 -dark-blue _margin-r-10 _margin-b-sm-5")
print(f'Localização: {local}')

tempMin = soup.find(id='min-temp-1')
print(f'A temperatura mínima é {tempMin.text}')

tempMax = soup.find(id='max-temp-1')
print(f'A temperatura máxima é {tempMax.text}')

resumo = soup.find(class_= '-gray -line-height-24 _center')
resumo = resumo.text.strip()
print(f'Resumo: {resumo}')

