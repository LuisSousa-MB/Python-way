import random

mock_bot_names = ["Juca","Tadeu","Zequinha","Marcia","Batatinha","Bernado","Maria Bonita","Ezequiel","Sonia","Seu Zé","Robert","Mario","Marta","Julia","Poppi","Josenildo","Will","Mr.Brown","Ronald"]


class Card:
    """Represents a standard playing card."""
    def __init__(self, naipe=0, rank=2):
        self.naipe = naipe
        self.rank = rank
    
    naipes = ['♣', '♦', '♥', '♠']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.naipes[self.naipe])
    def __lt__(self, other):
        t1 = self.naipe, self.rank
        t2 = other.naipe, other.rank
        return t1 < t2

class Baralho:

    def __init__(self):
        self.cards = []
        for naipe in range(4):
            for rank in range(1, 14):
                card = Card(naipe, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
            
novoBaralho = Baralho()

novoBaralho.shuffle()

#print(novoBaralho)

player_1_cards = []
player_2_cards  = []
player_3_cards  = []
player_4_cards  = []

players = []
players_cards = [player_1_cards ,player_2_cards , player_3_cards , player_4_cards] 
jogando = True

def novosBots():
    for i in range(1,4):
        name = random.randint(0, len(mock_bot_names))
        players.append(mock_bot_names[name])

def novasCartas():
    cartas = []
    for card in novoBaralho.cards:
        cartas.append(str(card))
    return cartas

def distribuiCartasParaplayers_cards(cartas):
    for i in range(1,3):
        for player in players_cards:
            player.append(cartas[-1])
            cartas.pop()

def cartasIniciasParaMesa(cartas):
     for i in range(1,4):
        mesa.append(cartas[-1])
        cartas.pop()
        
def exibeCartasFechadas():
    num = 0
    for player in players_cards:
        print("Cartas do {}".format(players[num]))
        for card in player:
            if num == 0:
                print(card)
            else:
                print("************")
        num += 1 

def exibeMesa():
    for card in mesa:
        print(card)

def embaralha(cartas):
    random.shuffle(cartas)

def vez(vez):
    if vez == 1:
        pass

def primeraFase():
    pass

print("Defina o nome do jogador: ")
jogador = input()
players.append(jogador)

while jogando:

  

    novoBaralho.shuffle()
    embaralhadas = novasCartas()
    mesa = []
    #print(embaralhadas)
    novosBots()

    distribuiCartasParaplayers_cards(embaralhadas)

    print("")  

    exibeCartasFechadas()
    
    cartasIniciasParaMesa(embaralhadas)

    print("\nMesa:")
    exibeMesa()
    embaralha(embaralhadas)

    while len(mesa) < 5:
        pass
    jogando = False