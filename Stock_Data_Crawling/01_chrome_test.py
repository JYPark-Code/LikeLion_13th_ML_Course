from urllib.request import urlopen
from bs4 import BeautifulSoup

# 01. 우리가 가져올 URL
# 02. 내가 원하는 정보의 위치 (span, id)
# URL: https://finance.naver.com/sise/
# Tag: span, id : KOSPI_now

# Html 코드 요청해서 가져온다.
url = "https://finance.naver.com/sise/"
page = urlopen(url)
print(page)

# 구체적인 html 확인하고, 구조화
soup = BeautifulSoup(page, 'html.parser')
KOSPI = soup.find("span", id="KOSPI_now")
KOSDAQ = soup.find("span", id="KOSDAQ_now")
KPI200 = soup.find("span", id="KPI200_now")

print("현재 코스피 지수는 : ", KOSPI.text)
print("현재 코스닥 지수는 : ", KOSDAQ.text)
print("현재 코스피200 지수는 : ", KPI200.text)

# 인기 종목
popularItems = soup.find("ul", class_="lst_pop")
pop_stock_name = popularItems.find_all("a")
pop_stock_num = popularItems.find_all("span", class_="dn")

for item in pop_stock_name:
    print(item.text)

for value in pop_stock_num:
    print(value.text)