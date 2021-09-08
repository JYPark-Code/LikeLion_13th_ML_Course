from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import glob
import os
import time

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page,"lxml")
# print(soup.title)

# csv, Excel 만들기
current_date_hour = time.strftime('%y%m%d_%H', time.localtime(time.time()))

def write_csv_excel(filename, input_data):
    data = pd.DataFrame({f"{filename}": input_data})
    data.to_csv(f"{current_date_hour}{filename}.csv", index=False)
    data.to_excel(f"{current_date_hour}{filename}.excel.xlsx", index=False)

# 코스피 정보 가져오기
kospi_num = soup.find("em", id="now_value")
print("실시간 코스피 지수 : ", kospi_num.text)

# 거래량 천주 정보 가져오기
deal_info = soup.find("td", id="quant")
print("코스피(천주) 거래량 : ", deal_info.text)

# 장중 최고 , 52주최고
high_value = soup.find("td", id="high_value")
print("장중 최고 : ", high_value.text)

high_table = soup.find("table", class_="table_kos_index")
td_in_high = high_table.find_all("td", class_="td")
fifty_two_high = td_in_high[2]
print("52주 최고 : ", fifty_two_high.text)
# fifty_two_high = soup.find("")


# 추가 정보 - 투자자별 매매동향
investor_program_info = soup.find("dl", class_="lst_kos_info")
investor_shell_info = investor_program_info.find_all("dd", class_="dd")

for investor in investor_shell_info:
    print(investor.text)
    
# 추가 정보 - 시황 뉴스 게시글 제목
si_hwang_list = soup.find_all("ul", class_="sise_report")
si_hwang_news = si_hwang_list[0]
news_title = si_hwang_news.find_all("a", href=True)

# print("-----시황뉴스 게시글-----")
news_title_list = []
for title in news_title:
    news_title_list.append(title.text)

# pandas로 csv 만들기

# data = pd.DataFrame({"시황뉴스": news_title_list})
# print(data)
# data.to_csv("news.csv", index=False)
# data.to_excel("news.excel.xlsx", index=False)

# 추가 정보 - 시황정보 리포트
si_hwang_report = si_hwang_list[1]
report_title = si_hwang_report.find_all("a", href=True)

print("-----시황정보 리포트-----")
news_report_list = []
for title in report_title:
    news_report_list.append(title.text)


# 추가 정보 - 인기검색어 & 가장 많이 본 뉴스
right_boxes = soup.find_all("div", class_="box_type_r")
# print(len(right_boxes))
ranked_list = right_boxes[0]
# print(ranked_list)
ranked_list_companies = ranked_list.find_all("a", class_="company")
ranked_list_companies_stock = ranked_list.find_all("td", class_="number")
# print(ranked_list_companies)
# 인기 검색어 회사명:
company_list = []
for company in ranked_list_companies:
    company_list.append(company.text)
# print(company_list)
# 인기 검색어 회사 주:
company_stocks = []
for stock in ranked_list_companies_stock:
    company_stocks.append(stock.text)
# print(company_stocks)
combined_list = [list(a) for a in zip (company_list,company_stocks)]
# print(combined_list)

# 가장 많이 본 뉴스:
popular_news_box = right_boxes[1]
pop_news_title = popular_news_box.find_all("a")
# print(pop_news_title)
pop_news_list = []
for title in pop_news_title:
    pop_news_list.append(title.text)

pop_news_list = pop_news_list[1:] # 더보기 삭제
# print(pop_news_list)

# 파일 만들기
# write_csv_excel("시황뉴스", news_title_list)
# write_csv_excel("시황정보_리포트", news_report_list)
# write_csv_excel("인기검색어", combined_list)
# write_csv_excel("가장_많이_본_뉴스", pop_news_list)

# 한 파일로 병합

path = os.getcwd()
all_files = glob.glob(os.path.join(path, "*.csv"))
all_data = []
for file in all_files:
    df = pd.read_csv(file)
    all_data.append(df)
merged_df = pd.concat(all_data, axis=0, ignore_index=True, sort=True)
merged_df.to_csv(f"{current_date_hour}병합파일.csv", index=False)


# 지수 정보 파일 하나 만들기
# 시황정보 뉴스 20210908_14_news.csv
# 시황정보 리포트 20210908_14_report.csv
# 인기검색어 20210908_14_pop_word.csv
# 가장 많이 본 뉴스 20210908_14_cnt_new.csv