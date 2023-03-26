from validate_docbr import CPF

class Cpf:
    

    def __init__(self,documento):
        documento = str(documento)
        self.validador = CPF()

        if self.cpf_valido(documento):
            self.cpf = self.formata_cpf(documento)
        else:
            raise ValueError("CPF inválido!!!")
    
    def __str__(self):
        return self.cpf

    def cpf_valido(self, documento):
        if len(documento) == 11:
            return self.validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida!!!")

    def formata_cpf(self, documento):
        return self.validador.mask(documento)