import pandas as pd
import seaborn as sns
t = sns.load_dataset("titanic")

df_titan = pd.DataFrame(t)
# print(df_titan)
t_cols = df_titan.columns
# print(t_cols)
ppl = df_titan.count(axis=0).max()
print("     타이타닉 호 리포트      ")
print("---------------------------")
print("탑승 인원수 : ", ppl, "명")
survived = df_titan["survived"]
print("생존자 인원 수 : ", survived.sum(), '명')
female_passenger_df = df_titan[df_titan["sex"] == "female"]
male_passenger_df = df_titan[df_titan["sex"] == "male"]

male_pass_count = male_passenger_df.count(axis=0).max()
female_pass_count = female_passenger_df.count(axis=0).max()
print("---------------------------")
print("총 남자 승객수: ", male_pass_count, "명")
print("총 여자 승객수: ", female_pass_count, "명")

male_survivor_df = df_titan.loc[(df_titan["sex"] == "male") & df_titan["survived"]]
# print(male_survivor_df)
male_survivor_count = male_survivor_df.count().max()

female_survivor_df = df_titan.loc[(df_titan["sex"] == "female") & df_titan["survived"]]
# print(male_survivor_df)
female_survivor_count = female_survivor_df.count().max()
print("---------------------------")
print("남자 생존자수: ", male_survivor_count, "명")
print("여자 생존자수: ", female_survivor_count, "명")

first_passenger_df = df_titan[df_titan["pclass"] == 1]
second_passenger_df = df_titan[df_titan["pclass"] == 2]
third_passenger_df = df_titan[df_titan["pclass"] == 3]

first_ppl = first_passenger_df.count().max()
second_ppl = second_passenger_df.count().max()
third_ppl = third_passenger_df.count().max()
print("---------------------------")

print("1등석 인원: ", first_ppl, "명")
print("2등석 인원: ", second_ppl, "명")
print("3등석 인원: ", third_ppl, "명")