from validate_docbr import CNPJ

class Cnpj:
    

    def __init__(self,documento):
        documento = str(documento)
        self.validador = CNPJ()

        if self.cnpj_valido(documento):
            self.cnpj = self.formata_cnpj(documento)
        else:
            raise ValueError("CNPJ inválido!!!")
    
    def __str__(self):
        return self.cnpj

    def cnpj_valido(self, documento):
        if len(documento) == 14:
            return self.validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida!!!")

    def formata_cnpj(self, documento):
        return self.validador.mask(documento)

    def gerar_cnpj(self):
        return self.validador.generate()