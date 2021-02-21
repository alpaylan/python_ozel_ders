import pandas as pd

df = pd.read_csv('archive/heart.csv')
print(df)

df_data = df.drop(columns=['target'])
# print(df_data)

df_target = df.get('target')

print(df_target)
