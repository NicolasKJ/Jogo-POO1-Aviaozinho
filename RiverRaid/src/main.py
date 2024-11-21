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
cor_branco = (35, 35, 35)
cor_preto = (0, 0, 0)

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

#Pontos
pontos = 000

#Fonte
fonte = pygame.font.SysFont('space', 40, True, False)

# Colocando legenda no topo da tela
pygame.display.set_caption('River Raid')

tela = pygame.display.set_mode(tamanho_tela)
tela.fill(cor_branco)


aviao = Aviao()

imagem_path_aviao = os.path.join(os.getcwd(), '..', 'assets', 'images', 'aviao.png')
imagem_path_barco1 = os.path.join(os.getcwd(), '..', 'assets', 'images', 'barco4.png')
imagem_path_barco2 = os.path.join(os.getcwd(), '..', 'assets', 'images', 'barco2.png')
imagem_path_barco3 = os.path.join(os.getcwd(), '..', 'assets', 'images', 'barco3.png')
imagem_path_barco4 = os.path.join(os.getcwd(), '..', 'assets', 'images', 'barco4.png')


imagem_aviao = pygame.image.load(imagem_path_aviao).convert_alpha()
tela.blit(imagem_aviao, (aviao.x, aviao.y))

inimigo_1 = Inimigos(200, 50)
imagem_inimigo1 = pygame.image.load(imagem_path_barco1).convert_alpha()
tela.blit(imagem_inimigo1, (inimigo_1.x, inimigo_1.y))

velocidade = 1

while True:
    velocidade += 0.001

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura o estado das teclas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        aviao.x += 3
        if aviao.x > 539:
            aviao.x = 539

    if teclas[pygame.K_LEFT]:
        aviao.x -= 3
        if aviao.x < -20:
            aviao.x = -20

    if teclas[pygame.K_UP]:
        aviao.y -= 3
        if aviao.y < -5:
            aviao.y = -5

    if teclas[pygame.K_DOWN]:
        aviao.y += 3
        if aviao.y > 650:
            aviao.y = 650

     #Mensagem
    mensagem = f'{pontos:03}'
    texto_formatado = fonte.render(mensagem, True, (cor_preto))

    #Colisao bullets com inimigo
    #if bullet.colliderect(inimigo): #tem que colocar esse coliderect na entity
        #pontos += 50


    # Deixando a tela em branco novamente
    tela.fill(cor_branco)

    inimigo_1.movimentar(velocidade)

    tela.blit(imagem_aviao, (aviao.x, aviao.y))
    tela.blit(texto_formatado,(525, 20))
    tela.blit(imagem_inimigo1, (inimigo_1.x, inimigo_1.y))
    pygame.display.update()

    # Controlando o FPS

    # Controlando o FPS (frames por segundo)
    pygame.time.Clock().tick(60)
