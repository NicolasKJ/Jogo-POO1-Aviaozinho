class Aviao:
    def __init__(self, x=300, y=250):
        self.x = x
        self.y = y

    def mover(self, velocidade):
        self.x += velocidade
