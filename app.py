import requests

html = requests.get('https://www.climatempo.com.br/').content

print(html)