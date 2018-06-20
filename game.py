from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro
from evento import *


class Game(object):

    def __init__(self, tabuleiro, jogador, limite_jogadas=12):
        self.__tabuleiro = tabuleiro
        self.__jogador = jogador
        self.__limite_jogadas = limite_jogadas

    @property
    def jogador(self):
        return self.__jogador

    def executa_evento(self):
        eventos = [Macaco(), Gorila(), Vento(), Jacare(), Rinoceronte(), Nada(), Enchente()]
        eventos[randint(0, len(eventos))].executa(self)

    def jogar_dados(self):
        self.__jogador.andar_frente(int(randint(0, 6)))
        self.executa_evento()
        self.diminuir_jogadas()

    def diminuir_jogadas(self):
        self.__limite_jogadas -= 1


if __name__ == '__main__':

    g = Game(Tabuleiro(), Jogador(), 10)
    g.jogar_dados()

