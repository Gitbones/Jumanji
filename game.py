from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro
from evento import *


class Game(object):

    def __init__(self, tabuleiro, jogador, limite_jogadas=15):
        self.__tabuleiro = tabuleiro
        self.__jogador = jogador
        self.__limite_jogadas = limite_jogadas
        self.eventos = [Macaco(), Gorila(), Vento(), Jacare(), Rinoceronte(), Nada(), Enchente()]

    @property
    def jogador(self):
        return self.__jogador

    def executa_evento(self):
        self.eventos[randint(0, len(self.eventos) - 1)].executa(self)

    def jogar_dados(self):
        self.__jogador.andar_frente(int(randint(1, 6)))
        self.executa_evento()
        self.diminuir_jogadas(1)

    def diminuir_jogadas(self, value):
        self.__limite_jogadas -= value
        if(self.__limite_jogadas < 0):
            self.__limite_jogadas = 0

    def perder(self):
        return self.__limite_jogadas <= 0

    def ganhar(self):
        return self.__tabuleiro.qtd_casas <= self.__jogador.posicao

if __name__ == '__main__':

    g = Game(Tabuleiro(), Jogador())
    while(not g.ganhar() and not g.perder()):
        g.jogar_dados()
        print(g.jogador.posicao)
        if(g.ganhar()):
            print("Ganhou!")
            break
        elif(g.perder()):
            print("Perdeu!")
            break
