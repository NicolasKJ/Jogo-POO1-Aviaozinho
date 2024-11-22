class Fuel:
    def __init__(self, x, y=50):
        self.x = x
        self.y = y

    def movimentar(self, velocidade):
        self.y += velocidade
