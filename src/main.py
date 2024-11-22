import os.path
import random
import sys
import pygame
from entities.aviao import Aviao
from entities.inimigo import Inimigos
from entities.bullet import Bullet
from entities.fuel_bar import FuelBar

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

#barra combustivel
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

imagem_aviao = pygame.image.load(imagem_path_aviao).convert_alpha()
imagem_inimigo1 = pygame.image.load(imagem_path_barco1).convert_alpha()

inimigo_1 = Inimigos(200, 50)

balas = []
clock = pygame.time.Clock()

# Lista de inimigos
inimigos = []
tempo_criacao_inimigo = 2000  # Tempo entre inimigos em ms
ultimo_inimigo = 0


# Variável para controlar intervalo entre tiros
ultimo_tiro = 0
intervalo_tiro = 500  # em ms
jogo_pausado = False
velocidade = 1

# Loop Principal
while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            jogo_pausado = not jogo_pausado

    # Pausa do jogo
    if jogo_pausado:
        texto_pausa = fonte.render("PAUSADO", True, (255, 0, 0))
        tela.blit(texto_pausa, (tamanho_tela[0] // 2 - texto_pausa.get_width() // 2, tamanho_tela[1] // 2))
        pygame.display.update()
        clock.tick(fps)
        continue

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


    velocidade += 0.001
    #barra de combustivel
    dt = clock.tick(60) / 1000
    fuel_bar.update(dt)

    # Controle de disparo
    agora = pygame.time.get_ticks()
    if teclas[pygame.K_SPACE] and (agora - ultimo_tiro > intervalo_tiro):
        nova_bala = Bullet(aviao.x + imagem_aviao.get_width() // 2 - 2, aviao.y)
        balas.append(nova_bala)
        ultimo_tiro = agora

    # Criar novos inimigos
    if agora - ultimo_inimigo > tempo_criacao_inimigo:
        x_random = random.randint(0, tamanho_tela[0] - imagem_inimigo1.get_width())
        novo_inimigo = Inimigos(x_random, 0)
        inimigos.append(novo_inimigo)
        ultimo_inimigo = agora

    # Atualizar inimigos
    for inimigo in inimigos[:]:
        inimigo.movimentar(velocidade)

        # Verifica se saiu da tela
        if inimigo.y > tamanho_tela[1]:
            inimigos.remove(inimigo)

    # Mensagem de pontos
    mensagem = f'{pontos:03}'
    texto_formatado = fonte.render(mensagem, True, cor_preto)

    # Colisão bullets com inimigo
    for bala in balas[:]:
        bala_rect = pygame.Rect(bala.x, bala.y, 5, 10)  
        for inimigo in inimigos[:]:  
            inimigo_rect = pygame.Rect(inimigo.x, inimigo.y, imagem_inimigo1.get_width(), imagem_inimigo1.get_height())
            if bala_rect.colliderect(inimigo_rect):  
                pontos += 50
                inimigos.remove(inimigo)  
                if bala in balas:
                    balas.remove(bala)  
                break  


    # Desenha elementos na tela
    tela.fill(cor_branco)  # Limpa a tela
    tela.blit(imagem_aviao, (aviao.x, aviao.y))  # Avião
    fuel_bar.draw(tela)
    tela.blit(texto_formatado, (525, 20))  #Pontuação

    # Desenhar inimigos
    for inimigo in inimigos:
        tela.blit(imagem_inimigo1, (inimigo.x, inimigo.y))

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
