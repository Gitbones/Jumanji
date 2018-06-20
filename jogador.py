import random


class Jogador(object):

    def __init__(self, nome="1", posicao=0):
        self.__nome = nome
        self.__posicao = posicao

    @property
    def nome(self):
        return self.__nome

    @property
    def posicao(self):
        return self.__posicao

    def andar_frente(self, value):
        self.__posicao += value

    def andar_tras(self, value):
        self.__posicao -= value