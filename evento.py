class Macaco(object):
    def executa(self, game):
        print("O macaco Twelves apareceu e roubou os dados. Fique uma rodada sem jogar.")
        game.diminuir_jogadas(1)

class Gorila(object):
    def executa(self, game):
        print("Um gorila te jogou longe. Volte uma casa.")
        game.jogador.andar_tras(1)

class Morcego(object):
    def executa(self, game):
        print("Um aglomerado de morcegos bloqueou a visão de seu adversário, aproveite e avance mais duas casas.")
        game.jogador.andar_frente(2)

class Vento(object):
    def executa(self, game):
        print("Um forte vento virou o dado e alterou sua jogada.  Ande o equivalente à sua jogada mais uma casa extra.")
        game.jogador.andar_frente(1)

class Jacare(object):
    def executa(self, game):
        print("Um jacaré mordeu seu pé. Fique duas rodada sem jogar.")
        game.diminuir_jogadas(2)

class Rinoceronte(object):
    def executa(self, game):
        print("Uma manada de rinocerontes veio em sua direção. Você fugiu e voltou duas casas.")
        game.jogador.andar_tras(2)

class Nada(object):
    def executa(self, game):
        print("Estranhamente, nada aconteceu. Prossegue sua jogada.")

class Enchente(object):
    def executa(self, game):
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