from bs4 import BeautifulSoup
from selenium import webdriver
import time

start = time.time()
import pandas as pd

current_date_hour = time.strftime('%y%m%d_%H', time.localtime(time.time()))

driver = webdriver.Chrome("./chromedriver.exe")
url = "https://datalab.naver.com/"
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")
# print(soup.title)

# 날짜 가져오기
date_all = soup.find_all("span", class_="title_cell")
# print(len(date_all))

date_list = []
for _ in date_all:
    if len(_.text):
        date_list.append(_.text)

print(date_list)
time.sleep(2)

# 문자열
# xpath = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[9]/div/div/ul/li[1]/a/span'
# sel_01 = driver.find_element_by_xpath(xpath)
# print(sel_01.text)

# 10개 가져오기
# pop_word = []
#
# for num in range(1, 11):
#     xpath_url = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[9]/div/div/ul/li[' + str(num) + ']/a/span'
#     one_ele = driver.find_element_by_xpath(xpath_url)
#     pop_word.append(one_ele.text)
#
# print(pop_word)


## 9월 9일
# 검색어1: //*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[9]/div/div/ul/li[1]/a/span
# 검색어3: //*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[9]/div/div/ul/li[3]/a/span
# 검색어7: //*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[9]/div/div/ul/li[7]/a/span
# 검색어10: //*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[9]/div/div/ul/li[10]/a/span

## 9월 12일
## //*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[12]/div/div/ul/li[1]/a/span
## //*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[12]/div/div/ul/li[2]/a/span


# four_day_lists = []
# for day in range(9, 13):
#     for num in range(1, 11):
#         xpath_s = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div['+ str(day) +']/div/div/ul/li[' + str(num) + ']/a/span'
#         one_ele = driver.find_element_by_xpath(xpath_s)
#         four_day_lists.append(one_ele.text)
# print(four_day_lists)


# left_button : //*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[1]/span
# right_button : //*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[2]/span

prev_click = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[1]/span'
next_click = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[2]/span'

go_left = driver.find_element_by_xpath(prev_click)
go_right = driver.find_element_by_xpath(next_click)

for i in range(len(date_list) - 4):
    go_left.click()
    if i % 2 == 0:
        time.sleep(1)
    else:
        time.sleep(1.5)

dict_all_data = {}

for day in range(1, 13):
    top_ten = []
    for num in range(1, 11):
        xpath_s = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[' + str(day) + ']/div/div/ul/li[' + str(num) + ']/a/span'
        one_ele = driver.find_element_by_xpath(xpath_s)
        top_ten.append(one_ele.text)

    print(top_ten)
    if day < 9:
        go_right.click()
    time.sleep(1.5)
    dict_all_data[date_list[day - 1]] = top_ten

# print(dict_all_data)

dat = pd.DataFrame(dict_all_data)
dat.to_csv(f"{current_date_hour}네이버_데이터랩.csv", index=False)
dat.to_excel(f"{current_date_hour}네이버_데이터랩.xlsx", index=False)
