import re 

""" padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"

email = re.search(padrao, texto)

print(email.group()) """

texto = "IW NET Telecom Ltda ME3,5(139) · Empresa de telecomunicaçãAv. Fernando Amaro Miranda, 403 · +12294267-0800 Fechado ⋅ Abre ter. às 08:00"


class TelefonesBR:

    def __init__(self, telefone):
        cod,telefone = self.validate(str(telefone))
        if telefone:
            self.telefone = self.format(str(telefone))
        else:
            raise ValueError ("Deu ruim")
        self.tipo = "nulo"
        self.cod_pais = cod

    def validate(self, telefone):
        padrao = "(\+[0-9]{2,3})?(\(*[0-9]{2}\)*[9]*[0-9]{4}-*[0-9]{4})"
        encontrado = re.search(padrao,telefone)
        if encontrado.group():
            if len(str(encontrado)) == 11:
                if encontrado[2] != "9":
                    raise ValueError ("Número de celular inválido!")
            if encontrado.group(1) != None:
                self.cod_pais = encontrado.group(1)
                return encontrado.group(1),encontrado.group(2)
            else:
                return "+55",encontrado.group(2)
        else:
            raise ValueError("Telefone inválido")
    def format(self, telefone):
        parenteses = True if telefone.find("\(") else False
        tem_traco = True if telefone.find("-") else False
        print(parenteses,tem_traco)
        if tem_traco:
            telefone = telefone.replace("-","")
        if parenteses:
            telefone = telefone.replace("(","")
            telefone = telefone.replace(")","")

        if len(telefone) == 11 :   
            self.tipo = "Celular"
            return "({}){}-{}".format(telefone[:2],telefone[2:7],telefone[-4:])
        else:
            self.tipo = "Fixo"

            return "({}){}-{}".format(telefone[:2],telefone[2:6],telefone[-4:])

    def __str__(self):
        return self.cod_pais + self.telefone

novo_telefone = TelefonesBR(texto)


print(novo_telefone)