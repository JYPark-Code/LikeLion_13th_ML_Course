import pandas as pd
import datetime
import os

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

corona = pd.read_csv(f"./data/{yesterday}_corona.csv")
vaccine = pd.read_csv(f"./data/{today}_vaccinated.csv")
country_code = pd.read_csv("./data/country.csv", encoding="cp949")
continent_ko = pd.read_csv("./data/continent_ko_only.csv", encoding="cp949")

# print(corona.shape, vaccine.shape, country_code.shape)

# print(corona["국가"].str.extract("([ㄱ-ㅎ | 가-힣]+)"))

corona["한글표기"] = corona["국가"].str.extract("([ㄱ-ㅎ | 가-힣]+)")

col = ['국가', '한글표기', '위중증_합계', '위중증1일', '치명(%)', '완치(%)', '발생률',
       '인구수', '확진자_합계', '확진자1일', '사망자_합계', '사망자1일', '완치_합계', '완치1일']

new_corona = corona[col].copy()
# print(new_corona)
# print(country_code.columns)
country_code.columns = ["kr_code", "en_code", "country", "etc"]
continent_ko.columns = ["year", "국가코드", "country_nm", "대륙"]
# print(country_code.head())
# print(new_corona.columns)

df_corona = new_corona.merge(country_code, left_on='한글표기', right_on='kr_code')
# print(df_corona.columns)

df_corona_mid = df_corona.merge(vaccine, left_on='en_code', right_on='국가')
df_corona_all = df_corona_mid.merge(continent_ko, left_on="한글표기", right_on='country_nm')

option = input("나라별 보고서 - 1, 국가코드,경제조합 포함 - 2 : ")

if int(option) == 1:
    df_corona_mid.drop(['국가_x'], axis=1, inplace=True)
    df_corona_mid.drop(['국가_y'], axis=1, inplace=True)
    df_corona_all.drop(['country'], axis=1, inplace=True)
    df_corona_all.drop(['etc'], axis=1, inplace=True)
    today = datetime.date.today()
    path_dir = os.getcwd() + "\\data\\"
    path_file = path_dir + str(today)
    df_corona_mid.to_csv(path_file + "_merged.csv", index=False)
    df_corona_mid.to_excel(path_file + "_merged.xlsx", index=False)

elif int(option) == 2:
    df_corona_all.drop(['국가_x'], axis=1, inplace=True)
    df_corona_all.drop(['국가_y'], axis=1, inplace=True)
    df_corona_all.drop(['year'], axis=1, inplace=True)
    df_corona_all.drop(['country'], axis=1, inplace=True)
    df_corona_all.drop(['etc'], axis=1, inplace=True)
    df_corona_all.drop(['country_nm'], axis=1, inplace=True)
    today = datetime.date.today()
    path_dir = os.getcwd() + "\\data\\"
    path_file = path_dir + str(today)
    df_corona_all.to_csv(path_file + "_merged_continent_.csv", index=False)
    df_corona_all.to_excel(path_file + "_merged_continent_.xlsx", index=False)
