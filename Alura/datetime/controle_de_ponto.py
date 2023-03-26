from datetime import datetime,timezone,date,timedelta


data_atual = date.today()


#print("{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year))

data_em_texto = data_atual.strftime("%d/%m/%Y")

print(data_em_texto)

""" Uma das vantagens da classe datetime é que ela consegue cuidar da data e do horário ao mesmo tempo.
A única diferença em nosso uso é que, em vez do método today(), usaremos o método now(): """

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")

print(data_e_hora_em_texto)

""" Se tivéssemos uma string de data e quiséssemos transformar em datetime, 
o que faríamos?Novamente, um simples método resolve tudo, dessa vez o strptime(), da própria
classe datetime: """

#data_e_hora_em_texto = "01/03/2018 12:30"
#data_e_hora = datetime.strptime(data_em_texto, "%d/%m/%Y %H:%M")


""" Não podemos deixar que o tempo no nosso programa dependa de cada máquina, porque não temos como garantir 
que todas as máquinas que rodarem esse programa estarão com o fuso horário que queremos. O ideal, então, seria forçar 
o fuso horário de São Paulo.

Fuso horário com a classe timezone
A partir do Python 3, temos a classe timezone, também do módulo datetime: """

data_e_hora_atuais = datetime.now()

diferenca = timedelta(hours=-3)
print(diferenca)

fuso_horario = timezone(diferenca) #offset -3 = São paulo UTC -3
""" O parâmetro offset representa a diferença entre o fuso horário que queremos criar e o Tempo Universal Coordenado (UTC). 
No nosso caso, em São Paulo, temos uma diferença de -3 horas, mais conhecida como UTC-3. 
 """
print(fuso_horario)

data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M:%S")

print(data_e_hora_sao_paulo_em_texto)


""" Resolvendo o problema dos fusos horários com o pytz
A comunidade Python, frente a essa necessidade, criou diversas bibliotecas para facilitar a manipulação 
de timezones, como a pytz. Para instalar a pytz, você pode usar o pip pelo terminal:

pip install pytz
A instalação em sistemas baseados em UNIX provavelmente necessitará de permissão sudo.

Instalada, podemos importar sua classe timezone e fica fácil de pegarmos o fuso horário que queremos:

from datetime import datetime
from pytz import timezone

data_e_hora_atuais = datetime.now()
fuso_horario = timezone("America/Sao_Paulo")
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

print(data_e_hora_sao_paulo_em_texto)
Repare que nós colocamos o timezone como America/Sao_Paulo. Mas e se quisermos saber outras possibilidades? É possível ver a lista de fusos horários suportados pelo pytz iterando sobre o pytz.all_timezones:

import pytz

for tz in pytz.all_timezones:
    print(tz) """

#****************************************************************************#

""" Mais Python e Datas
Ao longo desse post, usamos diversas vezes alguns códigos de formatação de datas, como por exemplo o 
padrão %d/%m/%Y %H:%M. Mas o que significa isso?

Esses códigos são definidos pela documentação do strftime(3). Os usados em nossos exemplos são:

%d - O dia do mês representado por um número decimal (de 01 a 31)
%m - O mês representado por um número decimal (de 01 a 12)
%Y - O ano representado por um número decimal incluindo o século
%H - A hora representada por um número decimal usando um relógio de 24 horas (de 00 a 23)
%M - O minuto representado por um número decimal (de 00 a 59) """