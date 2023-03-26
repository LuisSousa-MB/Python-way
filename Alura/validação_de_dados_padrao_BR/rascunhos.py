from Cpf import Cpf
from Cnpj import Cnpj
from validate_docbr import CNPJ

gerCnpj = CNPJ()
cpf_1 = 40150162898
cnpj_1 = gerCnpj.generate()

object_cpf = Cpf(cpf_1)
object_cnpj = Cnpj(cnpj_1)

print(object_cpf, "\n",object_cnpj)