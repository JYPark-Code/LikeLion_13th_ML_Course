# List
myfood = ['banana', 'apple', 'candy']
# print(myfood[0])
# print(myfood[1])
# print(myfood[2])
# print(myfood[1:3])

#
# for item in myfood:
#     print(item)

# 딕셔너리 (dict)
dict1 = {'one': '하나', 'two': '둘', 'three': '셋'}
dict2 = {1: '하나', 2: '둘', 3: '셋'}
dict3 = {'co11': [1, 2, 3], 'col2': ['a', 'b', 'c']}

# print(dict1['one'])
# print(dict2[2])
# print(dict3['col2'])

# 판다스 모듈 불러오기
import pandas as pd
import matplotlib as mpl
from pandas import Series

# print("pandas 버전 : ", pd.__version__)
# print("matplotlib 버전 : ", mpl.__version__)

# Series 만들기 -> ___ = Series([1000, 14000, 3000, 100000])

# score = Series([1000, 14000, 30000, 10000])
# print(score)
# print(type(score))
#
# print(score.index)
# print(list(score.index))
# print(score.values)
#
# print(type(score.index))
# print(type(list(score.index)))
# print(type(score.values))

# score = Series([1000, 14000, 3000],
#                index=["2019-05-01", "2019-05-02", "2019-05-03"])
# print(score)

# score = Series(['a', 'b', 'c'])
# print(score)
#
# score_idx = Series(['a', 'b', 'c'],
#                    index=["2019-09-16", "2019-09-17", "2019-09-18"])
# print(score_idx)
#
# for idx in score.index:
#     print(idx)
#
# for value in score.values:
#     print(value)

# gildong = Series([1500, 3000, 2500],
#                   index=["2019-05-01", "2019-05-02", "2019-05-03"])
#
# toto = Series([3000, 2000, 2000],
#                index=["2019-05-01", "2019-05-02", "2019-05-03"])
# print(gildong + toto)


idx = pd.date_range(start="2020-01-01", end="2020-01-03").tolist()

# score_idx = Series(['a', 'b', 'c'],
#                    index=idx)
# print(score_idx)

ninty = pd.date_range(start="2021-01-01", end="2021-03-31").tolist()
ninty_idx = Series(list(map(int, range(1, 91))),
                   index=ninty)
# print(ninty_idx)

# 데이터 프레임의 이해
'''
* Pandas(판다스)의 대표적인 기본 자료형
* Seaborn 데이터 (load_dataset() - 판다스)
    * seaborn에 들어가는 기본적인 데이터 자료형 pandas
* plotly에서도 pandas 호환  
'''

idx_date = pd.date_range(start="2020-01-01", end="2020-01-04").tolist()

from pandas import DataFrame

dat = {'col1': [1, 2, 3, 4],
       'col2': [10, 20, 30, 40],
       'col3': ['A', 'B', 'C', 'D']}

df = DataFrame(dat, index=idx_date)
# print(df)


team_score = {"toto": [1500, 3000, 5000, 7000, 5500],
              "apple": [4000, 5000, 6000, 5500, 4500],
              "gildong": [2000, 2500, 3000, 4000, 3000],
              "catanddog": [7000, 5000, 3000, 5000, 4000]}

team_df = DataFrame(team_score)
# print(team_df)

# print(team_df['catanddog'])

# 두개의 열 선택
select_two = ['catanddog', 'toto']
# print(team_df[select_two])
# print(team_df[['catanddog', 'toto']])

# 두개의 열 선택
# team_df.loc[] # 해당 이름으로 검색
# team_df.iloc[] # 인덱스로 선택

# print(team_df.loc[ [0, 2, 4] , ['toto','gildong']])

idx_date = pd.date_range(start="2019-05-01", end="2019-05-05").tolist()
team_df.index = idx_date

# print(team_df.loc['2019-05-02'])  # 19-05-02 일
# print("-----------")
# print(team_df.loc[['2019-05-02', '2019-05-03']])  # 5월 2일, 3일
# print("-----------")
# print(team_df.loc['2019-05-02':])  # 5월 2일 이후 전체 데이터 가져오기
# print("-----------")
# print(team_df)
# print("-----------")
# print(team_df.sum(axis=0)) # index 별 합 (0), column 별 합 : (1)

# print(team_df.mean())
# print(team_df.std())
# print(team_df.max())
# print(team_df.min())
#
# print(team_df[['apple', 'catanddog']].sum())
# print("-----------")
# print(team_df[['apple', 'catanddog']].mean())
# print("-----------")
# print(team_df[['apple', 'catanddog']].std())
# print("-----------")
#
#
team_df["Rows_sum"] = team_df.iloc[:, :4].sum(axis=1)
# print(team_df)

import seaborn as sns
t = sns.load_dataset("titanic")

df_titan = pd.DataFrame(t)
# print(df_titan)

# print(team_df)

# print(team_df.Rows_sum.sort_values(ascending=False))

team_df["Rows_mean"] = team_df.iloc[:, :4].mean(axis=1)
# print(team_df)
team_df["Rows_median"] = team_df.iloc[:, :4].median(axis=1)
# print(team_df)

print(team_df.loc['2019-05-03':].loc[(team_df["Rows_sum"] >= 15000)])

# print(team_df.loc[(team_df["Rows_sum"] >= 15000) & (team_df["Rows_mean"] >= 4000), : ])