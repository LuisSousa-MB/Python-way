class Datas():

    def __init__(self,dia,mes,ano):
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano
    
    def formata(self):
        print("{}/{}/{}".format(self.__dia,self.__mes,self.__ano))