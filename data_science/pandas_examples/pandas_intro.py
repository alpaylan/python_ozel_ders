import pandas as pd

df = pd.read_csv("../data.csv")

print(df)
print(df[['X', 'Y']])

df.to_numpy()
