from acesso_cep import BuscarEndereco

cep = "04849567"

objeto_cep = BuscarEndereco(cep)

print(objeto_cep.format_cep())
objeto_cep.busca_endereço()