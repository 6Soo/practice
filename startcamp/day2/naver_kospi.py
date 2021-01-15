import requests
from bs4 import BeautifulSoup


# 1. url
url = 'https://finance.naver.com/main/main.nhn'
# 2. url 로 요청을 보낸다.
response = requests.get(url).text
# print(type(response))
# 3. 받은 응답을 예쁘게 꾸며준다.
data = BeautifulSoup(response, 'html.parser')
# 4. 꾸민 응답중에서 원하는 데이터를 선택.
result = data.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num').text
print(result)