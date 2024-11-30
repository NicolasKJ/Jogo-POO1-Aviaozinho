class Aviao:
    def __init__(self, x=300, y=350, morreu=False):
        self.x = x
        self.y = y
        self.morreu = morreu

    def mover(self, velocidade):
        self.x += velocidade
