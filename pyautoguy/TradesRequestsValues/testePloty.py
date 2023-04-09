import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import time

# Inicializar dados vazios
data = {'USDEUR': [], 'USDJPY': [], 'USDCAD': []}

# Loop de monitoramento (por exemplo, a cada minuto)
while True:
    # Receber novos dados
    new_data = {'USDEUR': 0.9229, 'USDJPY': 127.86, 'USDCAD': 1.3394}
    # Adicionar novos dados ao conjunto de dados
    for currency in data:
        data[currency].append(new_data[currency])
    # Criar um DataFrame a partir dos dados
    df = pd.DataFrame(data)
    # Criar o gráfico
    fig = make_subplots(rows=1, cols=1)
    for currency in data:
        fig.add_trace(go.Scatter(x=df.index, y=df[currency], name=currency))
    # Atualizar o gráfico
    fig.update_layout(title='Cotações em Tempo Real')
    fig.show()
    # Aguardar antes de receber novos dados
    time.sleep(60)
