from Cnpj import Cnpj
from Cpf import Cpf
from validate_docbr import CNPJ, CPF

#Instancias para teste
gera_cnpj = CNPJ()
gera_cpf = CPF()

#Factory para CNPJ ou CPF
class Gera_doc():

    @staticmethod
    def tipo_doc(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida.")
        
#Objetos para teste
novo_doc_A = Gera_doc.tipo_doc(gera_cnpj.generate())
novo_doc_B = Gera_doc.tipo_doc(gera_cpf.generate())

print(novo_doc_A)
print(novo_doc_B)