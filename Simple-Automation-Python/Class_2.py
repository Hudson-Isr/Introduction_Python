import pandas as pd
import plotly.express as px

#1. importação da tabela e drop de colunas. 

tabela = pd.read_csv(r"C:\Users\Hudson Israel\Downloads\telecom_users.csv")
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela = tabela.drop("IDCliente", axis=1)
#tabela = tabela.drop("Codigo", axis=1).

#2. Tratamentos de dados.

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
#Drop Coluna.
tabela = tabela.dropna(how= "all",axis= 1) #all = todos valores vazio.

#Drop Linha.
tabela = tabela.dropna(how= "any",axis= 0) #any = pelo menos um valor vazio.

#3. Análise inicial.
print(tabela["Churn"].value_counts()) #Será mostrado quantas pessoas cancelaram.

#Normalize=true mostrar o percentual, .map("{:.1%}".format) = Formular de como formatar em percentual.
print(tabela["Churn"].value_counts(normalize=True).map())

#4. Análise completa
#Etapa 1 criar o gráfico 


#for coluna in tabela.columns:
grafico = px.histogram(tabela, x= "Dependentes")

#Etapa 2 Ixibir o gráfico 
grafico.show()
