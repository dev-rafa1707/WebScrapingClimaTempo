import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/1310/franciscobeltrao-pr').text

soup = BeautifulSoup(html, 'html.parser')


local = soup.find(class_ = 'city _margin-r-5 -font-13')
print(f'Localização: {local.text}')

tempMin = soup.find(id='min-temp-1')
print(f'A temperatura mínima é {tempMin.text}')

tempMax = soup.find(id='max-temp-1')
print(f'A temperatura máxima é {tempMax.text}')

resumo = soup.find(class_= '-gray -line-height-24 _center')
resumo = resumo.text
resumo = resumo.strip()
print(f'Resumo: {resumo}')




