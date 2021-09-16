import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
t = sns.load_dataset("titanic")
data = pd.DataFrame(t)

'''
0 ~ 7.9104 - 1번 그룹
7.9104 ~ 14.4542 - 2번 그룹
14.4542 ~ 31 3번 - 3번 그룹
31 ~ 512 - 4번 그룹
'''

# data_fare01 = data.loc[(data.fare > 0) & (data.fare <= 7.9104), :]
# data_fare02 = data.loc[(data.fare > 7.9104) & (data.fare <= 14.4542), :]
# data_fare03 = data.loc[(data.fare > 14.4542) & (data.fare <= 31), :]
# data_fare04 = data.loc[(data.fare > 31) & (data.fare <= 512), :]

data.loc[ (data.fare >=0) & (data.fare <= 7.9104)  , "group_fare"  ] = 1
data.loc[ (data.fare > 7.9104) & (data.fare <= 14.4542)  , "group_fare"  ] = 2
data.loc[ (data.fare > 14.4542) & (data.fare <= 31)  , "group_fare"  ] = 3
data.loc[ (data.fare > 31) & (data.fare <= 512)  , "group_fare"  ] = 4

# print(data["age"].min())
# print(data["age"].max())

'''
0 ~ 10 : u10
11 ~ 19 : 10s
21 ~ 29 : 20s
31 ~ 39 : 30s
...
61 ~ 80 : old_man

'''

data.loc[ (data.age >= 0) & (data.age < 10)  , "group_age"  ] = "10b"
data.loc[ (data.age >= 10) & (data.age < 20)  , "group_age"  ] = "10s"
data.loc[ (data.age >= 20) & (data.age < 30)  , "group_age"  ] = "20s"
data.loc[ (data.age >= 30) & (data.age < 40)  , "group_age"  ] = "30s"
data.loc[ (data.age >= 40) & (data.age < 50)  , "group_age"  ] = "40s"
data.loc[ (data.age >= 50) & (data.age < 60)  , "group_age"  ] = "50s"
data.loc[ (data.age >= 60) & (data.age < 70)  , "group_age"  ] = "60s"
data.loc[ (data.age >= 70) & (data.age < 80)  , "group_age"  ] = "70s"

# print(data)

under_10 = data[data["group_age"] == "10b"]
teens = data[data["group_age"] == "10s"]
twenties = data[data["group_age"] == "20s"]
thirties = data[data["group_age"] == "30s"]

plt.figure(figsize=(15,15))
plt.subplot(2, 2, 1)

# sns.boxplot(x="age", data=under_10)
# plt.show()
# sns.boxplot(x="age", data=teens)
# plt.show()
# sns.boxplot(x="age", data=twenties)
# plt.show()
# sns.boxplot(x="age", data=thirties)
# plt.show()

sel = ['pclass', 'sex', 'age', 'fare', 'group_fare']
group_by_gfare = data[sel].groupby(['group_fare']).count()
print(group_by_gfare)

# Group_by_check
group_by_gfare_mean = data.groupby(['group_fare']).mean()
group_by_gfare_sum = data.groupby(['group_fare']).sum()
group_by_gfare_med = data.groupby(['group_fare']).median()
group_by_gfare_cnt = data.groupby(['group_fare']).count()

# print(group_by_gfare_mean)

gb_age_mean = data.groupby(['group_age']).mean()
print(gb_age_mean)

gb_sex_class_port = data.groupby(['sex', 'pclass', 'embarked']).count()
print(gb_sex_class_port)