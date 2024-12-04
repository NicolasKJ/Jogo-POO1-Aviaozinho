class Inimigos:
    def __init__(self, x, y, tipo, vida=2, vivo=True):
        self.x = x
        self.y = y
        self.tipo = int(tipo)
        self.vida = vida
        self.vivo = vivo

    def movimentar(self, velocidade):
        self.y += velocidade
