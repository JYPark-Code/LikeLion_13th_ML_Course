from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import random
import time
import date_picker

# 테이블 데이터 추출
def table_extract(app_length, sales_on):
    total_list = []
    for rank in range(1, app_length + 1):
        app_info = []
        dyn_app_name = driver.find_element_by_xpath(
            f'//*[@id="page-scroll-obj"]/section/table/tbody/tr[{str(rank)}]/td[2]/span/span/span[1]')
        dyn_dev = driver.find_element_by_xpath(
            f'//*[@id="page-scroll-obj"]/section/table/tbody/tr[{str(rank)}]/td[2]/span/span/span[2]')

        if sales_on:
            dyn_feature_1 = driver.find_element_by_xpath(
                f'//*[@id="page-scroll-obj"]/section/table/tbody/tr[{str(rank)}]/td[3]/div/p[1]/span')
            dyn_feature_2 = driver.find_element_by_xpath(
                f'//*[@id="page-scroll-obj"]/section/table/tbody/tr[{str(rank)}]/td[3]/div/p[2]/span')
            dyn_feature_3 = driver.find_element_by_xpath(
                f'//*[@id="page-scroll-obj"]/section/table/tbody/tr[{str(rank)}]/td[3]/div/p[3]/span')

        else:
            dyn_feature_1 = driver.find_element_by_xpath(
                f'//*[@id="page-scroll-obj"]/section/table/tbody/tr[{str(rank)}]/td[3]/span')
            dyn_feature_2 = driver.find_element_by_xpath(
                f'//*[@id="page-scroll-obj"]/section/table/tbody/tr[{str(rank)}]/td[4]')
            dyn_feature_3 = driver.find_element_by_xpath(
                f'//*[@id="page-scroll-obj"]/section/table/tbody/tr[{str(rank)}]/td[5]')



        # 5개 정보 저장
        app_info.append(dyn_app_name.text)
        app_info.append(dyn_dev.text)
        app_info.append(dyn_feature_1.text.strip())
        app_info.append(dyn_feature_2.text.strip())
        app_info.append(dyn_feature_3.text.strip())

        # 총 리스트에 저장
        total_list.append(app_info)
        if rank % 2 == 0:
            time.sleep(0.5)
        else:
            time.sleep(0.4)
    return total_list


url = "https://www.mobileindex.com/mi-chart/top-100/overall"
driver = webdriver.Chrome('./chromedriver')

# Global time sleep
driver.implicitly_wait(3)

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')

# 날짜 선택 - 모듈
date_picker.date_picking(driver)
time.sleep(3)

# print(soup.title)
# 기록할 현재_날짜_시간
current_date_hour = time.strftime('%y%m%d_%H', time.localtime(time.time()))

# 데이터상 날짜
target_date = driver.find_element_by_xpath(
    '//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span/span').text
# print(target_date.text)


#  날짜 뽑아 내기
#  날짜 변경 하기

# [일간] 2021-09-11 매출 순위 1위 기준 Xpath
# ---------------------
# 앱 이름 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[2]/span/span/span[1]
# 개발사 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[2]/span/span/span[2]

# 구글 순위 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[3]/div/p[1]/span
# 애플 순위 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[3]/div/p[2]/span
# 원스토어 순위 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[3]/div/p[3]/span

# 매출 순위 2위 기준 Xpath
# ---------------------
# 앱 이름 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[2]/td[2]/span/span/span[1]
# 개발사 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[2]/td[2]/span/span/span[2]

# 구글 순위 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[2]/td[3]/div/p[1]/span
# 애플 순위 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[2]/td[3]/div/p[2]/span
# 원스토어 순위 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[2]/td[3]/div/p[3]/span

# 매출 순위 1위 Xpath로 가져와 보기. - 성공
# app_name = driver.find_element_by_xpath('//*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[2]/span/span/span[1]')
# develop_co = driver.find_element_by_xpath(
#     '//*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[2]/span/span/span[2]')
#
# google_rank = driver.find_element_by_xpath('//*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[3]/div/p[1]/span')
# apple_rank = driver.find_element_by_xpath('//*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[3]/div/p[2]/span')
# one_rank = driver.find_element_by_xpath('//*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[3]/div/p[3]/span')

# print(app_name.text)
# print(develop_co.text)
# print(google_rank.text)
# print(one_rank.text)

info_table = soup.find_all("table")
app_table = info_table[0]
app_rows = app_table.find_all("tr")
# 앱 개수 = 총 갯수 - 헤더
total_app_count = len(app_rows) - 1

# print(len(app_rows))

# 매출 데이터 추출
print_both = input("")
sales_rank = table_extract(total_app_count, True)


# 출력해보기
df = pd.DataFrame(data=sales_rank, columns=["앱명", "개발사", "구글스토어 순위", "애플스토어 순위", "원스토어 순위"])
df.to_csv(f"{target_date}_앱스토어_매출순위_모바일인덱스.csv")
df.to_excel(f"{target_date}_앱스토어_매출순위_모바일인덱스.xlsx")

# 사용자 순위 추출하기.

user_button = driver.find_element_by_xpath('//*[@id="root"]/article/div/div[3]/div/button[1]')
user_button.click()
time.sleep(5)
# [일간] 2021-09-11 사용자 순위 1위 기준 Xpath
# 앱 이름 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[2]/span/span/span[1]
# 개발사 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[2]/span/span/span[2]

# 상세정보
# 상승률 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[3]/div/span
# 업종 대분류 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[4]
# 업종 소분류 : //*[@id="page-scroll-obj"]/section/table/tbody/tr[1]/td[5]

# 위와 동일한 구조.
usage_rank = table_extract(total_app_count, False)

df = pd.DataFrame(data=usage_rank, columns=["앱명", "개발사", "구글스토어 순위", "애플스토어 순위", "원스토어 순위"])
df.to_csv(f"{target_date}_앱스토어_사용자_수_순위_모바일인덱스.csv")
df.to_excel(f"{target_date}_앱스토어_사용자_수_순위_모바일인덱스.xlsx")

