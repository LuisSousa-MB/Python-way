from bytebank import Funcionario
import pytest
from pytest import mark #Marks são tags que ajudam a gerenciar os testes.

class TestClass:
    @mark.idade
    def test_quando_idade_recebe_22_07_2000_deve_retornar_23(self):
        entrada = "22/07/2000"  #Given-Contexto
        esperado = 23           #define Then-Desfecho

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-Ação

        assert resultado == esperado # Then-Desfecho
    
    @mark.nome
    def test_quando_nome_recebe_Milena_Costa_de_Sousa_deve_retornar_Milena_Costa_de_Sousa(self):
        entrada = "Milena Costa de Sousa"
        esperado = "Milena Costa de Sousa"

        milena = Funcionario(entrada, "22/07/2000", 1330)

        resultado = milena.nome

        assert resultado == esperado

    @mark.diretores
    def test_quando_sobrenome_recebe_Milena_Costa_de_Sousa_deve_retornar_Sousa(self):
        entrada = "Milena Costa de Sousa"
        esperado = "Sousa"

        milena = Funcionario(entrada, "22/07/2000", 1330)

        resultado = milena.sobrenome()

        assert resultado == esperado

    @mark.decrescimo
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000
        entrada_nome = "Paula Roberta Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/11/1998", entrada)
        funcionario_teste.descrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_ateh_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario("teste", "11/11/1998", entrada)
        resultado = funcionario_teste.bonus()

        assert resultado == esperado

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_mais_do_que_10000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10001

            funcionario_teste = Funcionario("teste", "11/11/1998", entrada)
            resultado = funcionario_teste.bonus()

            assert resultado 

    """ @mark.print
    def test_deve_retornar_o_str(self):
        nome, data_nascimento, salario = "teste", "11/11/1998", 1200
        funcionario_teste = Funcionario(nome, data_nascimento, salario)

        esperado = f'NOME: {nome}\nIDADE: {funcionario_teste.idade()} \nSALARIO: {salario}'

        resultado = funcionario_teste.__str__()

        assert resultado == esperado
 """