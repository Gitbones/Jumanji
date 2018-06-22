from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro
from evento import *


class Game(object):

    #Inicia as classes que serão utilizadas e o limite de jogadas permitidas
    def __init__(self, tabuleiro, jogador, limite_jogadas=15):
        self.__tabuleiro = tabuleiro
        self.__jogador = jogador
        self.__limite_jogadas = limite_jogadas
        self.eventos = [Macaco(), Gorila(), Vento(), Jacare(), Rinoceronte(), Nada(), Enchente()]

    @property
    def jogador(self):
        return self.__jogador

    @property
    def limite_jogadas(self):
        return self.__limite_jogadas

    def executa_evento(self):
        self.eventos[randint(0, len(self.eventos) - 1)].executa(self)

    #Cria a função do dado d6 e do seu movimento. Já atualização a posição do jogador
    #e o numero de jogadas máximo
    def jogar_dados(self):
        valor = int(randint(1, 6))
        self.jogador.andar_frente(valor)
        print("Você tirou {} e está agora na posição {}".format(valor, self.jogador.posicao))
        self.executa_evento()
        self.diminuir_jogadas(1)

    def diminuir_jogadas(self, value):
        if(self.__limite_jogadas - value <= 0):
            self.__limite_jogadas = 0
        else:
            self.__limite_jogadas -= value

    def perder(self):
        return self.__limite_jogadas == 0

    def ganhar(self):
        return self.__tabuleiro.qtd_casas == self.__jogador.posicao


if __name__ == '__main__':
#Laço principal do jogo, criando as entradas do usuáros e saídas do sistema.
    g = Game(Tabuleiro(), Jogador())
    while(not g.ganhar() and not g.perder()):
        print("Aperte ENTER para jogar os dados!")
        input()
        g.jogar_dados()

        print("A sua posição é: {}".format(g.jogador.posicao))
        print("Você ainda tem {} jogadas\n".format(g.limite_jogadas))
        if(g.ganhar()):
            print("Parabéns você GANHOU!")
            break
        elif(g.perder()):
            print("Perdeu e ficou preso para sempre em JUMANJI!")
            break
