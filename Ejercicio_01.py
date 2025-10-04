import pandas as pd

data = {'Nombre': ['Ignacio', 'María', 'Juan'], 'Edad': [53, 45, 13]}
df = pd.DataFrame(data)

print(df["Nombre"])

for i in range(len(df)):
    print(df["Nombre"][i])

print(type(df))