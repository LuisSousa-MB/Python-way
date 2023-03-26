""" Conhecendo a rich comparison
No Python temos como implementar algo similar ao equals(), mas ainda mais poderoso - a comparação rica, ou, como é tecnicamente conhecida, rich comparison . Com ela, podemos definir os seguintes métodos de comparação em uma classe:

__eq__(), chamado pelo operador ==
__ne__(), chamado pelo operador !=
__gt__(), chamado pelo operador >
__lt__(), chamado pelo operador <
__ge__(), chamado pelo operador >=
__le__(), chamado pelo operador <=
No nosso caso, como estamos tratando de comparações de igualdade, focaremos no método __eq__() (mas é importante notar a possibilidade de implementação de todos os tipos básicos de comparação!).

Precisamos, primeiro, saber o que queremos que seja comparado. Como precisamos que a comparação foque em algo único de cada filme, usaremos o próprio título. Então vamos implementar:
 """

class Filme():

    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def __str__(self):
        return self.titulo + " - " + self.diretor

    def __eq__(self, outro_filme): #implementação do __eq__
        return self.titulo == outro_filme.titulo

filmes_de_terror = []

o_monstro = Filme("O monstro","Josézinho")
a_criatura = Filme("A critatura","Maria Tereza")
o_palhaço = Filme("O Palhaço","Severino Zacarias")

filmes_de_terror.append(o_monstro)
filmes_de_terror.append(a_criatura)
filmes_de_terror.append(o_palhaço)

filmes_de_acao = []

atire_e_corra = Filme("Atire e Corra","João do Bairro")
luz_camera_e_tiros = Filme("Luz, camêra e tiros!","Suzy Bonnada")
o_delegado = Filme("O Delegado","Lucas Leoncio")

filmes_de_acao.append(atire_e_corra)
filmes_de_acao.append(luz_camera_e_tiros)
filmes_de_acao.append(o_delegado)


def pega_todos_os_filmes():
    todos_os_filmes = []
    for filme in filmes_de_terror:
        todos_os_filmes.append(filme)
    for filme in filmes_de_acao:
        todos_os_filmes.append(filme)
    return todos_os_filmes

meus_filmes = pega_todos_os_filmes()
for filme in meus_filmes:
    print(filme)


""" Simplificando nossa verificação com o operador in
Podemos, ainda, simplificar o código em nossa função tenho_o_filme() utilizando o operador in para verificar se
 o filme já está na lista, já que este operador também se baseia no retorno de ==: """

def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    if filme_procurado in meus_filmes: #uso do __eq__ através do operador "in"
        print("Tenho o filme!")
    else:
        print("Não tenho :(")

filme_procurado1 = Filme("A Teoria de Tudo", "James Marsh")

filme_procurado2 = Filme("O Delegado", "James Marsh")

tenho_o_filme(filme_procurado1)

tenho_o_filme(filme_procurado2)