import pandas as pd

df_dict = {'name': ['Johnny', 'Bobby', 'Happy', 'Tammy', 'Pammy', 'Jenny', 'Peter']
            , 'gender': ['male', 'male', 'female', 'female', 'female', 'female', 'male']
            , 'phone': ['android', 'iphone', 'iphone', 'iphone', 'iphone', 'android', 'android']
            , 'bill': [70, 60, 45, 55, 90, 75, 35]
            , 'state': ['NY', 'CA', 'CA', 'CA', 'NY', 'CA', 'NY']
            , 'age': [35, 42, 29, 26, 23, 19, 31]
}

df = pd.DataFrame(df_dict)

print(df['phone'].value_counts())




# print(df['age'].mean())
# print(df['age'].median())
# print(df['age'].std())

# 'user name' # column name with space 
# df['user name']




















# lst1 = [1, 2, 3, 4, 5]
# tup1 = (1, 2, 3, 4)
# dict1 = {1: 'a'
#     , 2: 'b'
#     , 3: 'c'
# }

# print(lst1[0])
# print(dict1[3])