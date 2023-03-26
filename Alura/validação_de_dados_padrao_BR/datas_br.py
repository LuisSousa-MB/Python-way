from datetime import datetime, timedelta

class DatasBR:
    def __init__(self) :
        self.momento_cadastro = datetime.today()

    def get_mes_cadastro (self):
        mes_cadastro = self.momento_cadastro.month - 1
        mes_do_ano = [
             "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        return mes_do_ano[mes_cadastro]
    
    def get_dia_semana(self):
        dia_da_semana = [
            "Segunda-feira","Terça-feira", "Quarta-feira", "Quinta-feira","Sexta-feira","Sabado","Domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()

        return dia_da_semana[dia_semana]

    def get_data_formatoBR(self):
        dia_semana = self.get_dia_semana()
        mes = self.get_mes_cadastro()
        data_br_format_A = self.momento_cadastro.strftime("{}, dia %d de {} de %Y - %H:%M:%S").format(dia_semana, mes)
        data_br_format_B= self.momento_cadastro.strftime("%d/%m/%Y - %H:%M:%S")

        print(data_br_format_A,"\n",data_br_format_B)

    def get_tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=7)) - self.momento_cadastro
        print(tempo_cadastro)
        return tempo_cadastro