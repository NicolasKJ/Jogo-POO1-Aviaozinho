import pygame


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = -12
        self.largura = 5 
        self.altura = 10
        self.cor = (255, 0, 0) 

    def mover(self):
        self.y += self.velocidade

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    def fora_da_tela(self):
        return self.y < 0  # Saiu pela parte superior
