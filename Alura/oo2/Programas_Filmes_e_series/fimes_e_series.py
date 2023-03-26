class Programa:   #Classe mãe
    def __init__(self,titulo, ano):
        self._titulo = titulo.title()
        self._ano = ano
        self._likes = 0

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self,novotitulo):
        self._titulo = novotitulo.title()
    @property
    def likes(self):
        return self._likes
    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return "Titulo: {}\nAno: {}\nLikes: {}\n\n".format(self._titulo, self._ano, self._likes)
    


class Filme(Programa): # (*)herança

    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano)
        self._duracao = duracao

    def __str__(self):
       return "Titulo: {}\nAno: {}\nDuração/min: {}\nLikes: {}\n".format(self._titulo, self._ano, self._duracao, self._likes)


class Serie(Programa):

    def __init__(self, titulo, ano, temporada):
        super().__init__(titulo, ano)
        self._temporada = temporada
    
    def __str__(self):
        return "Titulo: {}\nAno: {}\nTemporadas: {}\nLikes: {}\n".format(self._titulo, self._ano, self._temporada, self._likes)
    
class Playlist():
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

filme1 = Filme ("Titanic", 1998, 204)
for i in range (0,4):
    filme1.dar_likes () 

serie1 = Serie ("Lost", 2005, 8)
for i in range (0,7):
    serie1.dar_likes ()

serie2 = Serie("Um maluco no pedaço",1995, 5)
for i in range (0,12):
    serie1.dar_likes ()

filme2 = Filme ("O corvo", 1997, 147)
for i in range (0,4):
    filme1.dar_likes () 

filme3 = Filme ("Batman", 1999, 127)
for i in range (0,49):
    filme1.dar_likes () 

filme_e_series = [filme1, serie1, filme2, serie2]
playlist_para_sabado = Playlist("Para sabadár", filme_e_series)

""" for programa in filme_e_series:
    detalhe = programa._duracao if hasattr(programa, "_duracao") else programa._temporada
    print("{} - ano:{} - temporada/duracão: {}".format(programa._titulo,programa._ano, detalhe)) """
print(playlist_para_sabado._nome)
print("Tamanho: {}\n".format(len(playlist_para_sabado)))
print("Isso mesmo" if filme3 in playlist_para_sabado else "Não tem, não")
for programa in playlist_para_sabado:
    print(programa)