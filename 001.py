#packs
import pandas as pd
import os
#fuctions

#main
vendas = {
    "data": ['15/02/2023','16/02/2024'],
    "valor": [500,300],
    "produto": ['feijão','arroz'],
    "quantidade": [50,70]
}
#vendas_df = pd.DataFrame(vendas)

planilha_df = pd.read_excel('Musicas 2.xlsx')
planilha_df.dropna(inplace= True)
#name_df = planilha_df['Nome']
column = planilha_df['Animação']

os.system('cls')
print(planilha_df)
print(column)
print(planilha_df.loc[1:5])

 
