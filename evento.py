class Evento(object):

    def __init__(self):
        self.__repeticoes = 2

    def executa(self, game):
        self.__repeticoes -= 1
        if (self.__repeticoes == 0):
            game.eventos.remove(self)

class Macaco(Evento):
    def executa(self, game):
        super(Macaco, self).executa(game)
        print("O macaco Twelves apareceu e roubou os dados. Fique uma rodada sem jogar.")
        game.diminuir_jogadas(1)

class Gorila(Evento):
    def executa(self, game):
        super(Gorila, self).executa(game)
        print("Um gorila te jogou longe. Volte uma casa.")
        game.jogador.andar_tras(1)

class Morcego(Evento):
    def executa(self, game):
        super(Morcego, self).executa(game)
        print("Um aglomerado de morcegos bloqueou a visão de seu adversário, aproveite e avance mais duas casas.")
        game.jogador.andar_frente(2)

class Vento(Evento):
    def executa(self, game):
        super(Vento, self).executa(game)
        print("Um forte vento virou o dado e alterou sua jogada.  Ande o equivalente à sua jogada mais uma casa extra.")
        game.jogador.andar_frente(1)

class Jacare(Evento):
    def executa(self, game):
        print("Um jacaré mordeu seu pé. Fique duas rodada sem jogar.")
        game.diminuir_jogadas(2)

class Rinoceronte(Evento):
    def executa(self, game):
        super(Rinoceronte, self).executa(game)
        print("Uma manada de rinocerontes veio em sua direção. Você fugiu e voltou duas casas.")
        game.jogador.andar_tras(2)

class Nada(Evento):
    def executa(self, game):
        super(Nada, self).executa(game)
        print("Estranhamente, nada aconteceu. Prossegue sua jogada.")

class Enchente(Evento):
    def executa(self, game):
        super(Enchente, self).executa(game)
        print("Um enchente te deixou impossibilitado de se mover. Não jogue a próxima rodada")
        game.diminuir_jogadas(1)


'''
1 - O macaco Twelves apareceu e roubou os dados. Fique uma rodada sem jogar.
2 – Um gorila te jogou longe. Volte uma casa.
3 – Um aglomerado de morcegos bloqueou a visão de seu adversário, aproveite e avance mais duas casas.
4 – Um forte vento virou o dado e alterou sua jogada.  Ande o equivalente à sua jogada mais uma casa extra.
5 – Um jacaré mordeu seu pé. Fique duas rodada sem jogar.
6 – Uma manada de rinocerontes veio em sua direção. Você fugiu e voltou duas casas.
7 – Estranhamente, nada aconteceu. Prossegue sua jogada.
8 – Um enchente te deixou impossibilitado de se mover. Não jogue a próxima rodada
'''