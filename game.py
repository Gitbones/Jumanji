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
        eventos[randint(0, len(eventos) - 1)].executa(self)

    def jogar_dados(self):
        self.__jogador.andar_frente(int(randint(0, 6)))
        self.executa_evento()
        self.diminuir_jogadas(1)

    def diminuir_jogadas(self, value):
        self.__limite_jogadas -= value

    def perder(self):
        return self.__limite_jogadas <= 0

    def ganhar(self):
        return self.__tabuleiro.qtd_casas <= self.__jogador.posicao

if __name__ == '__main__':

    g = Game(Tabuleiro(), Jogador(), 10)
    g.jogar_dados()

