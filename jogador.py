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
        if(self.__posicao + value >= 30):
            self.__posicao = 30
        else:
            self.__posicao += value

    def andar_tras(self, value):
        if(self.__posicao - value <= 0):
            self.__posicao = 0
        else:
            self.__posicao -= value
