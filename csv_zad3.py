import pandas as pd

data = pd.read_csv('records.csv', delimiter=';')
print(data)

print(data.columns)
print(data.values)

print(type(data.values))
print(data.values[0])
print(data.items)