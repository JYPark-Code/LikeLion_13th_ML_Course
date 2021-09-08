from urllib.request import urlopen
from bs4 import BeautifulSoup

# url
# tag, id, class
# 다우산업지수, 나스닥 종합, S&P 500

# 다우산업지수 : ul, class="data_lst" id="worldIndexColumn1"
# dd, class:point_status

url = "https://finance.naver.com/world/"
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

data = soup.find("ul", class_="data_lst", id="worldIndexColumn1")

print(data)
