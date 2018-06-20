from jogador import Jogador


class Tabuleiro(object):

    def __init__(self, qtd_casas=30):
        self.__qtd_casas = qtd_casas

    @property
    def qtd_casas(self):
        return self.__qtd_casas

    def imprime(self, jogador):
        print('''
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +--- -+
        |     |
        |     |
        +-----+
        |     |
        |     |
        +-----+
        ''')
