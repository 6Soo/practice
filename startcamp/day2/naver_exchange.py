import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
#print(type(response))
data = BeautifulSoup(response, 'html.parser')
#print(type(data))
result = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(result)