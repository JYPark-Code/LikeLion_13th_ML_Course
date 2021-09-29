from selenium import webdriver
import time
import pandas as pd
import datetime
import os



driver = webdriver.Chrome('./chromedriver')

url = 'https://www.bloomberg.com/graphics/covid-vaccine-tracker-global-distribution/'
driver.get(url)

# //*[@id="dvz-table-global-vaccination"]/div[2]/div[2]/button
# //*[@id="dvz-table-global-vaccination"]/div[2]/div[2]/button
sel_more1 = driver.find_element_by_xpath('//*[@id="dvz-table-global-vaccination"]/div[2]/div[2]/button')
sel_more1.click()
time.sleep(1)

# //*[@id="dvz-table-usa-vaccination"]/div[2]/div[2]/button
sel_more2 = driver.find_element_by_xpath('//*[@id="dvz-table-global-vaccination"]/div[2]/div[2]/button')
sel_more2.click()

all_data = []

for i in range(1, 7, 1):
    data_col = []
    xpath = f'//*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr/td[{str(i)}]'
    sel_data = driver.find_elements_by_xpath(xpath)

    for dat in sel_data:
        data_col.append(dat.text)

    print(data_col)
    all_data.append(data_col)

# pandas 데이터처리 ------------------
pd.set_option("display.max_rows", 40)

dat_dict = {'국가': all_data[0],
            '백신접종수': all_data[1],
            'Enough_percent_people:': all_data[2],
            '1차접종': all_data[3],
            '2차접종': all_data[4],
            '일별접종수': all_data[5]
            }
dat_df = pd.DataFrame(dat_dict)

# 국가명 길이 체크
print(dat_df['국가'].str.len().unique())

# 국가명 길이가 1보다 낮은것 처리
print(dat_df.loc[dat_df["국가"].str.len() < 1, :])

dat_df = dat_df.loc[dat_df["국가"].str.len() > 1, :]

# 결측치 처리
col_all = dat_df.columns
for one in col_all:
    print("col name : ", one)
    print(dat_df.loc[dat_df[one] == '–', one].count())

    dat_df.loc[dat_df[one] == '–', one] = "-999"
    dat_df.loc[dat_df[one] == '<0.1', one] = "0.05"

# 결측치 확인 - 처리 완료
for one in col_all:
    print("col name : ", one)
    print(dat_df.loc[dat_df[one] == '–', one].count())
    print("\n")

# 쉼표 제거
dat_df["백신접종수"] = dat_df["백신접종수"].str.replace(",", "")
dat_df["일별접종수"] = dat_df["일별접종수"].str.replace(",", "")

# null값 체크

print(dat_df.isnull().sum())
print(dat_df.info)

sel_col = dat_df.columns

for one in sel_col:
    print("col name: ", one)

    if one != "국가":
        print("col type: ", dat_df[one].dtype)
        dat_df[one] = dat_df[one].astype("float32")
        print("col type: ", dat_df[one].dtype)

    print()

today = datetime.date.today()
path_dir = os.getcwd() + "\\data\\"
path_file = path_dir + str(today)
dat_df.to_csv(path_file + "_vaccinated.csv", index=False)
dat_df.to_excel(path_file + "_vaccinated.xlsx", index=False)