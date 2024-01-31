
# %%
import pandas as pd

arquivo = pd.DataFrame(pd.read_excel('dataset.xls'))

print(arquivo)
# %%

# teste salvar em csv
arquivo.to_csv('testando')

