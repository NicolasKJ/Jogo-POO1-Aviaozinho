import os.path
import sys

import pygame
import time
from entities.aviao import Aviao
from entities.inimigo import Inimigos
import os

"""
Acredito que precisamos criar duas classes principais:

1. Do avião controlado pelo usuário
2. Dos inimigos (barco ou aviões)
"""

# Constantes
fps = 60
tamanho_tela = (600, 700)

# Essa cor é no padrao RGB
cor_branco = (255, 255, 255)

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

# Colocando legenda no topo da tela
pygame.display.set_caption('River Raid')

tela = pygame.display.set_mode(tamanho_tela)
tela.fill(cor_branco)

aviao = Aviao()

imagem_path = os.path.join(os.getcwd(), '..', 'assets', 'images', 'aviao.png')

imagem_aviao = pygame.image.load(imagem_path).convert_alpha()
tela.blit(imagem_aviao, (aviao.x, aviao.y))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura o estado das teclas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        aviao.x += 3

    if teclas[pygame.K_LEFT]:
        aviao.x -= 3

    if teclas[pygame.K_UP]:
        aviao.y -= 3

    if teclas[pygame.K_DOWN]:
        aviao.y += 3

    # Deixando a tela em branco novamente
    tela.fill(cor_branco)

    tela.blit(imagem_aviao, (aviao.x, aviao.y))
    pygame.display.update()

    # Controlando o FPS

    # Controlando o FPS (frames por segundo)
    pygame.time.Clock().tick(60)

pygame.display.update()

time.sleep(5)
print('River Raid')

pygame.display.flip()
pygame.quit()
