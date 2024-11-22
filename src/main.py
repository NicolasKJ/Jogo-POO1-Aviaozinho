import os.path
import sys
import pygame
from entities.aviao import Aviao
from entities.inimigo import Inimigos
from entities.bullet import Bullet
from entities.fuel_bar import FuelBar
from entities.fuel import Fuel
from random import randint

# Constantes
fps = 60
tamanho_tela = (600, 700)

# Essa cor é no padrão RGB
cor_branco = (35, 35, 35)
cor_preto = (0, 0, 0)

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

pygame.display.set_caption('River Raid')
tela = pygame.display.set_mode(tamanho_tela)

# Pontos
pontos = 0

# Barra combustivel
fuel_bar = FuelBar(10, 10, 200, 20)

# Fonte
fonte = pygame.font.SysFont('space', 40, True, False)

# Colocando legenda no topo da tela
pygame.display.set_caption('River Raid')

# Inicializando entidades
aviao = Aviao()
tela.fill(cor_branco)

imagem_path_aviao = os.path.join(os.getcwd(), '..', 'assets', 'images', 'aviao.png')
imagem_path_barco1 = os.path.join(os.getcwd(), '..', 'assets', 'images', 'barco1.png')
imagem_path_fuel = os.path.join(os.getcwd(), '..', 'assets', 'images', 'fuel.png')

imagem_aviao = pygame.image.load(imagem_path_aviao).convert_alpha()
imagem_inimigo1 = pygame.image.load(imagem_path_barco1).convert_alpha()
imagem_fuel = pygame.image.load(imagem_path_fuel).convert_alpha()

inimigo_1 = Inimigos(200, 50)

balas = []
fuels = []
clock = pygame.time.Clock()

# Variável para controlar intervalo entre tiros
ultimo_tiro = 0
intervalo_tiro = 500  # em ms

velocidade = 1
taxa_geracao_fuel = 2 * 60  # em clocks

tempo = 0  # Quanto tempo foi percorrido em clocks

# Loop Principal
while True:
    tempo += 1
    velocidade += 0.001

    # Gerando combustivel
    if tempo % taxa_geracao_fuel == 0:
        combustivel = Fuel(randint(20, 550))  # 20
        fuels.append(combustivel)

    # Barra de combustivel
    dt = clock.tick(60) / 1000
    fuel_bar.update(dt)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura o estado das teclas
    teclas = pygame.key.get_pressed()

    # Movimento do avião
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

    # Controle de disparo
    agora = pygame.time.get_ticks()
    if teclas[pygame.K_SPACE] and (agora - ultimo_tiro > intervalo_tiro):
        nova_bala = Bullet(aviao.x + imagem_aviao.get_width() // 2 - 2, aviao.y)
        balas.append(nova_bala)
        ultimo_tiro = agora

    # Mensagem de pontos
    mensagem = f'{pontos:03}'
    texto_formatado = fonte.render(mensagem, True, cor_preto)

    # Colisão bullets com inimigo
    for bala in balas[:]:
        bala_rect = pygame.Rect(bala.x, bala.y, 5, 10)  # Dimensões da bala
        inimigo_rect = pygame.Rect(inimigo_1.x, inimigo_1.y, imagem_inimigo1.get_width(), imagem_inimigo1.get_height())
        if bala_rect.colliderect(inimigo_rect):  # Verifica colisão
            pontos += 50
            balas.remove(bala)

    # Atualiza o movimento do inimigo
    inimigo_1.movimentar(velocidade)

    # Desenha elementos na tela
    tela.fill(cor_branco)  # Limpa a tela

    indice_apagar = []

    # Atualiza o movimento do combustivel
    for i in range(len(fuels)):
        fuels[i].movimentar(velocidade)
        tela.blit(imagem_fuel, (fuels[i].x, fuels[i].y))
        if fuels[i].y > 700:
            indice_apagar.append(i)

    for i in indice_apagar:
        del fuels[i]

    tela.blit(imagem_aviao, (aviao.x, aviao.y))  # Avião
    fuel_bar.draw(tela)
    tela.blit(imagem_inimigo1, (inimigo_1.x, inimigo_1.y))  # Inimigo
    tela.blit(texto_formatado, (525, 20))  # Pontuação

    # Desenha e atualiza balas
    for bala in balas[:]:
        bala.mover()
        if bala.fora_da_tela():
            balas.remove(bala)
        else:
            bala.desenhar(tela)

    # Atualiza a tela
    pygame.display.update()

    # Controla o FPS
    clock.tick(fps)
