import os.path
import random
import sys
import pygame
from entities.aviao import Aviao
from entities.inimigo import Inimigos
from entities.bullet import Bullet
from entities.fuel_bar import FuelBar
from entities.fuel import Fuel
from random import randint
from menu import exibir_menu
# Constantes
fps = 250
tamanho_tela = (600, 700)

# Essa cor é no padrão RGB
cor_branco = (255, 255, 255)
cor_cinza = (50, 50, 50)
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
exibir_menu(tela, tamanho_tela, cor_branco, cor_preto)

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

# Lista de inimigos
inimigos = []
tempo_criacao_inimigo = 1000  # Tempo entre inimigos em ms
ultimo_inimigo = 0


# Variável para controlar intervalo entre tiros
ultimo_tiro = 0
intervalo_tiro = 500  # em ms
jogo_pausado = False
velocidade = 1
taxa_geracao_fuel = 2 * 60  # em clocks

tempo = 0  # Quanto tempo foi percorrido em clocks

# Loop Principal
while True:
    tempo += 1
    velocidade += 0.001

    # barra de combustivel
    dt = clock.tick(60) / 1000
    fuel_bar.update(dt)

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
        aviao.x += 6
        if aviao.x > 539:
            aviao.x = 539

    if teclas[pygame.K_LEFT]:
        aviao.x -= 6
        if aviao.x < -20:
            aviao.x = -20

    if teclas[pygame.K_UP]:
        aviao.y -= 6
        if aviao.y < -5:
            aviao.y = -5

    if teclas[pygame.K_DOWN]:
        aviao.y += 6
        if aviao.y > 650:
            aviao.y = 650

    # barra de combustivel
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

    # Cria combustivel
    if tempo % taxa_geracao_fuel == 0:
        combustivel = Fuel(randint(20, 550))
        fuels.append(combustivel)

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

    # Colisão combustivel com o aviao
    for index in range(len(fuels)):
        combustivel_rect = pygame.Rect(fuels[index].x, fuels[index].y, 38, 38)
        aviao_rect = pygame.Rect(aviao.x, aviao.y, imagem_aviao.get_width(), imagem_aviao.get_height())
        if aviao_rect.colliderect(combustivel_rect):
            fuel_bar.pegou_combustivel()
            del fuels[index]
            break



    # Desenha elementos na tela
    tela.fill(cor_cinza)  # Limpa a tela

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
