import requests
import time
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

class Monitoramento:
    def __init__(self):
        self.pares = ["USD-EUR","USD-JPY","USD-CAD"]
        self.ultimos_precos = {pair.replace('-',''): [] for pair in self.pares}
        self.parado = False
        self.intervalo = 5 # valor padrão de intervalo em segundos
        
    def adicionar_par(self, novo_par):
        self.pares.append(novo_par)
        3
    def remover_par(self, par_remover):
        self.pares.remove(par_remover)
        
    def get_forex_data(self):
        url = "https://economia.awesomeapi.com.br/last/"
        url += ','.join(self.pares)
        response = requests.get(url)
        dados = response.json()
        for key, value in dados.items():
            if str(key) not in self.ultimos_precos: 
                self.ultimos_precos[key] = [value["bid"]]
                #print("Last prices: {}".format(self.ultimos_precos))
            else:    
                self.ultimos_precos[key].append(value["bid"])
            print(f'{key}:')
            print(f'\tValor: {value["bid"]}')
            print(f'\tÚltima atualização: {value["create_date"]}')
        
    def gerar_grafico(self):
        # Criar um DataFrame a partir dos dados
        df = pd.DataFrame(self.ultimos_precos)
        # Criar o gráfico
        fig = make_subplots(rows=1, cols=1)
        for currency in self.ultimos_precos:
            fig.add_trace(go.Scatter(x=df.index, y=df[currency], name=currency))
        # Atualizar o gráfico
        fig.update_layout(title='Cotações em Tempo Real')
        fig.show()
        # Aguardar antes de receber novos dados
            
    def monitorar(self):
        while True  :
            self.get_forex_data()
            self.gerar_grafico()
            time.sleep(self.intervalo)

            
    def set_intervalo_monitoramento(self, novo_intervalo):
        self.intervalo = novo_intervalo

def main():
    monitor = Monitoramento()
    while True:
        print("Menu:")
        print("1 - Adicionar par")
        print("2 - Remover par")
        print("3 - Iniciar monitoramento")
        print("4 - Alterar intervalo de monitoramento")
        opcao = input()
        if opcao == "1":
            novo_par = input("Insira o novo par (ex: BTC-BRL): ")
            monitor.adicionar_par(novo_par)
        elif opcao == "2":
            par_remover = input("Insira o par a ser removido (ex: BTC-BRL): ")
            monitor.remover_par(par_remover)
        elif opcao == "3":
            monitor.monitorar()
        elif opcao == "4":
            novo_intervalo = int(input("Insira o novo intervalo em segundos: "))
            monitor.set_intervalo_monitoramento(novo_intervalo)

main()

