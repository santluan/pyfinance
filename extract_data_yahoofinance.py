from yahooquery import Ticker
import matplotlib.pyplot as plt

# Coleta os dados da ação
petr = Ticker("PETR4.SA")

# resgata todo o historico de cotacoes
data = petr.history(period="max").reset_index()

# Obtem os indicadores fundamentalistas
petr.income_statement()

funds = petr.income_statement() # obtendo a demonstracao de resultado
funds = funds.transpose()       # transpõe a matriz
funds.columns = funds.iloc[0,:] # renomeia as colunas
funds = funds.iloc[1:,:-1]      # seleciona os dados anuais
funds = funds.iloc[:,::-1]      # inverte a ordem das colunas
funds

# Salvando os dados em csv
data.to_csv("petr_historico.csv")
funds.to_csv("petr_fundamentals.csv")

# visualizando dados
plt.plot('date', 'adjclose', data=data)
