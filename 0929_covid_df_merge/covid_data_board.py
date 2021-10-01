from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pandas as pd
import datetime
import os


driver = webdriver.Chrome("./chromedriver")
url = "https://coronaboard.kr"
driver.get(url)
time.sleep(3)

d = datetime.datetime.now()
# 옵션 체크 -------------------------------------------
def option_on():
    # 옵션 체크 xpath
    option_button = driver.find_element_by_xpath("//*[@id='global-slide']/div/div[2]/div/div/button")
    # 웹상에 스크롤 되지 않은 상태에서 버튼을 누를 수 없어서 ActionChains 을 쓴다.
    ActionChains(driver).move_to_element(option_button).perform()
    option_button.click()
    time.sleep(0.5)
    # 치료중, 위중증, 인구수 체크하기
    # cond_in_cure = driver.find_element_by_xpath('//*[@id="bs-select-1-0"]')
    # cond_in_cure.click()
    time.sleep(0.5)
    cond_in_serious = driver.find_element_by_xpath('//*[@id="bs-select-1-1"]')
    cond_in_serious.click()
    time.sleep(0.5)
    cond_pop = driver.find_element_by_xpath('//*[@id="bs-select-1-5"]')
    cond_pop.click()


option_on()
# 어제 클릭--------------------------------
# 어제 : //*[@id="global-slide"]/div/div[2]/ul/li[2]/a
flag_today = False  # False : 어제, Today : 오늘

if not flag_today:
    sel_yesterday = driver.find_element_by_xpath('//*[@id="global-slide"]/div/div[2]/ul/li[2]/a')
    sel_yesterday.click()

# 더보기 클릭-------------------------------
some_tag = driver.find_element_by_id('show-more')
ActionChains(driver).move_to_element(some_tag).perform()
some_tag.click()
some_tag = driver.find_element_by_id('show-more')
ActionChains(driver).move_to_element(some_tag).perform()
some_tag.click()

sel_country = driver.find_elements_by_xpath('//*[@id="country-table"]/div/div/table/tbody/tr/td[2]')
len(sel_country)

for one in sel_country:
    print(one.text)

all_data = []
for i in range(2, 11):
    tmp = '//*[@id="country-table"]/div/div/table/tbody/tr/td[{}]'.format(i)
    # print(tmp)
    sel_ele = driver.find_elements_by_xpath(tmp)

    column_data = []
    for one in sel_ele:
        # print(one.text)
        column_data.append(one.text)

    print(len(sel_ele))
    all_data.append(column_data)
    print(column_data)
    print()

print(all_data)

dict_dat = {"국가": all_data[0],
            "확진자": all_data[1],
            "위중증": all_data[2],
            "사망자": all_data[3],
            "완치": all_data[4],
            "치명(%)": all_data[5],
            "완치(%)": all_data[6],
            "발생률": all_data[7],
            "인구수": all_data[8]
            }
dat = pd.DataFrame(dict_dat)

# 데이터 전처리---
dat['위중증_합계'] = dat['위중증'].str.split('\n').str[0]
dat['위중증1일'] = dat['위중증'].str.split('\n').str[1]

dat['확진자_합계'] = dat['확진자'].str.split('\n').str[0]
dat['확진자1일'] = dat['확진자'].str.split('\n').str[1]

dat['사망자_합계'] = dat['사망자'].str.split('\n').str[0]
dat['사망자1일'] = dat['사망자'].str.split('\n').str[1]

dat['완치_합계'] = dat['완치'].str.split('\n').str[0]
dat['완치1일'] = dat['완치'].str.split('\n').str[1]

dat = dat.drop(['확진자', '사망자', '완치'], axis=1)

dat['위중증'] = dat['위중증'].str.replace(pat=r'[,()]', repl=r'', regex=True)
dat['발생률'] = dat['발생률'].str.replace(pat=r'[,]', repl=r'', regex=True)
dat['인구수'] = dat['인구수'].str.replace(pat=r'[,]', repl=r'', regex=True)

dat['위중증_합계'] = dat['위중증_합계'].str.replace(pat=r'[,]', repl=r'', regex=True)
dat['위중증1일'] = dat['위중증1일'].str.replace(pat=r'[,()]', repl=r'', regex=True)

dat['확진자_합계'] = dat['확진자_합계'].str.replace(pat=r'[,]', repl=r'', regex=True)
dat['확진자1일'] = dat['확진자1일'].str.replace(pat=r'[,()]', repl=r'', regex=True)

dat['완치_합계'] = dat['완치1일'].str.replace(pat=r'[,()]', repl=r'', regex=True)
dat['완치1일'] = dat['완치1일'].str.replace(pat=r'[,()]', repl=r'', regex=True)

dat['사망자_합계'] = dat['사망자_합계'].str.replace(pat=r'[,()]', repl=r'', regex=True)
dat['사망자1일'] = dat['사망자1일'].str.replace(pat=r'[,()]', repl=r'', regex=True)

# csv, xlsx 자료 만들기 ----------------------------------
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# print(today)
# print(yesterday)
if flag_today:
    file_make_time = today
else:
    file_make_time = yesterday

print( file_make_time )

print( os.getcwd() )
path_dir = os.getcwd() + "\\data\\corona\\"
path_file = path_dir + str(file_make_time)
print( path_dir,  path_file, sep="\n" )


dat.to_csv(path_file + "_corona.csv", index=False)
dat.to_excel(path_file + "_corona.xlsx", index=False)
os.listdir( path_dir )

