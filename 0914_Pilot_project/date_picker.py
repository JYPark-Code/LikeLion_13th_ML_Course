from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
from datetime import date


def date_picking(driver):
    selected_year, selected_month, selected_date = map(int, input("데이터를 구할 날짜를 적어주세요 (2021-9-11) : ").split('-'))
    today_check = datetime.datetime.now()

    # url = "https://www.mobileindex.com/mi-chart/top-100/overall"
    # driver = webdriver.Chrome('./chromedriver')

    # Global time sleep
    # driver.implicitly_wait(3)
    #
    # driver.get(url)
    # soup = BeautifulSoup(driver.page_source, 'lxml')

    # ------------------------------------------------

    date_button = driver.find_element_by_xpath('//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span')
    date_button.click()
    time.sleep(2)
    # sub-tree 를 사용해서 사라지는 element 잡아냈고
    # 연도 버튼 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[1]/label
    # 연도 버튼 활성화 후:
    # (최상단) 2019년 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[1]/span/button[1]
    # 2020년 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[1]/span/button[2]
    # 2021년 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[1]/span/button[3]

    # 월 버튼 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[2]
    # 월 버튼 활성화 후 :
    # (최상단) 1월 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[2]/span/button[1]
    # 2월 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[2]/span/button[2]
    # 3월 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[2]/span/button[3]

    # 달력 최상단 좌측 (일요일) : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/table/tbody/tr[1]/td[1]
    # 달력 최상단 다음 날짜 (월요일) : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/table/tbody/tr[1]/td[2]
    # 9월 11일 2번째 주 토요일 (2,7) : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/table/tbody/tr[2]/td[7]

    # 날짜만 뽑아내면 : //*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/table/tbody//td

    year_choose_button = driver.find_element_by_xpath(
        '//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[1]/label')

    if selected_year == 2019 or selected_year == 2020:
        year_choose_button.click()
        year_2019 = driver.find_element_by_xpath(
            '//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[1]/span/button[1]')
        year_2020 = driver.find_element_by_xpath(
            '//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[1]/span/button[2]')

        if selected_year == 2019:
            year_2019.click()
        elif selected_year == 2020:
            year_2020.click()

    month_choose_button = driver.find_element_by_xpath(
        '//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[2]')

    if int(today_check.month) != selected_month:
        month_choose_button.click()
        driver.find_element_by_xpath(
            '//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/span/span[2]/'
            f'span/button[{selected_month}]').click()

    # 날짜 선택
    y_info = (datetime.date(selected_year, selected_month, selected_date).weekday() + 2) % 7

    week_count = driver.find_elements_by_xpath(
        '//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/table/tbody/tr')

    for each_week in range(1, len(week_count) + 1):
        choosing_date = driver.find_element_by_xpath(
            f'//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/table/tbody/tr[{each_week}]/td[{y_info}]')
        if int(choosing_date.text) == selected_date:
            choosing_date.click()
            break

# (2,5)
# sep_ninth = driver.find_element_by_xpath(
#     f'//*[@id="page-scroll-obj"]/section/div[1]/div[2]/div[2]/span/span[2]/span/table/tbody/tr[2]/td[{y_info}]')
# sep_ninth.click()
