class Inimigos:
    def __init__(self, x, y, vida=2, vivo=True):
        self.x = x
        self.y = y
        self.vida = vida
        self.vivo = vivo

    def movimentar(self, velocidade):
        self.y += velocidade
