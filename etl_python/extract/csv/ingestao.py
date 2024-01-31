import pandas as pd

# copiar url do arquivo csv
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"

df = pd.read_csv(url)  # ler com pandas

df = pd.DataFrame(df)  # transformar em dataframe pandas

print(df)  # exibir

# salvar em um novo arquivo
df.to_csv('arquivo')
