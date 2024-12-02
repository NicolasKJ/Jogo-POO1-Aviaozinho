class Fundo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def movimentar(self, velocidade):
        self.y += velocidade
