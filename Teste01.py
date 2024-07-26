#packs
import matplotlib as plt
import pandas as pd

#Importações de dados
dado_df = pd.read_excel('Tabela 1.xlsx')
dados_RJ = dado_df.loc[dado_df['Local'] == 'Unidade RJ']
devolucao_Rj = dados_RJ['Devoluções']

#functions
def Grafico_rio():
    graf = devolucao_Rj.hist()


#Main
print(dado_df)
print(dados_RJ)
print('-'* 50)
print(devolucao_Rj)
Grafico_rio()
