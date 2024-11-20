import pygame
import time

"""
Acredito que precisamos criar duas classes principais:

1. Do avião controlado pelo usuário
2. Dos inimigos (barco ou aviões)
"""


class Aviao:
    pass


class Inimigos:
    pass


# Constantes
fps = 60
tamanho_tela = (640, 480)

# Essa cor é no padrao RGB
cor_branco = (255, 255, 255)

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

# Colocando legenda no topo da tela
pygame.display.set_caption('River Raid')

tela = pygame.display.set_mode(tamanho_tela)
tela.fill(cor_branco)

# Definindo a classe AviaoLocalizacao
class AviaoLocalizacao:
    def __init__(self, x, y):
        self.x = x  # Atributo x
        self.y = y  # Atributo y

aviao_localizacao = AviaoLocalizacao(155, 125)
imagem_aviao = pygame.image.load('aviao.png').convert_alpha()
tela.blit(imagem_aviao, (aviao_localizacao.x, aviao_localizacao.y))

pygame.display.update()

time.sleep(5)
print('River Raid')

pygame.display.flip()
pygame.quit()
