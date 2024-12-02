import os.path
import random
import sys
import pygame
from entities.fundo import Fundo
from entities.aviao import Aviao
from entities.inimigo import Inimigos
from entities.bullet import Bullet
from entities.fuel_bar import FuelBar
from entities.fuel import Fuel
from random import randint
from entities.menu import exibir_menu
from entities.game_over import morreu

# Constantes
fps = 200
tamanho_tela = (600, 700)

# Essa cor é no padrão RGB
cor_branco = (255, 255, 255)
cor_cinza = (50, 50, 50)
cor_preto = (0, 0, 0)

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

# Som
disparo_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), '..', 'assets', 'sounds', 'pew.mp3'))
combustivel_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), '..', 'assets', 'sounds', 'abastecer.mp3'))
fundo_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), '..', 'assets', 'sounds', 'musica_fundo.mp3'))

# Tocando sempre a musica
pygame.mixer.music.load("../assets/sounds/musica_fundo.mp3")
pygame.mixer.music.play(-1)

pygame.display.set_caption('River Raid')
tela = pygame.display.set_mode(tamanho_tela)

imagem_path_aviao = os.path.join(os.getcwd(), '..', 'assets', 'images', 'aviao.png')
imagem_path_nave1 = os.path.join(os.getcwd(), '..', 'assets', 'images', 'nave_1.png')
imagem_path_nave2 = os.path.join(os.getcwd(), '..', 'assets', 'images', 'nave_2.png')
imagem_path_nave3 = os.path.join(os.getcwd(), '..', 'assets', 'images', 'maicon.png')
imagem_path_fuel = os.path.join(os.getcwd(), '..', 'assets', 'images', 'fuel.png')
imagem_path_fundo = os.path.join(os.getcwd(), '..', 'assets', 'images', 'tela_fundo.png')

imagem_aviao = pygame.image.load(imagem_path_aviao).convert_alpha()
imagem_nave1 = pygame.image.load(imagem_path_nave1).convert_alpha()
imagem_nave2 = pygame.image.load(imagem_path_nave2).convert_alpha()
imagem_nave3 = pygame.image.load(imagem_path_nave3).convert_alpha()
imagem_fuel = pygame.image.load(imagem_path_fuel).convert_alpha()
imagem_fundo = pygame.image.load(imagem_path_fundo).convert_alpha()

while True:
    # Pontos
    pontos = 0

    # Barra combustivel
    fuel_bar = FuelBar(10, 10, 200, 20)

    # Fonte
    fonte = pygame.font.SysFont('space', 40, True, False)

    # Colocando legenda no topo da tela
    pygame.display.set_caption('River Raid')

    exibir_menu(tela, tamanho_tela, cor_branco, cor_preto)

    # Inicializando entidades
    aviao = Aviao()
    tela.fill(cor_branco)

    fundos = []
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
    taxa_geracao_fuel = 3.5 * 60  # em clocks

    # Variavel para determinar a aleatoriedade da geracao de inimigos
    fim = 60

    tempo = 0  # Quanto tempo foi percorrido em clocks

    # Loop Principal
    while True:
        
        if aviao.morreu:
            break

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
        
        # Mensagem de pontos
        mensagem = f'{pontos:03}'
        texto_formatado = fonte.render(mensagem, True, cor_branco)

        tempo += 1
        velocidade += 0.0015

        if len(fundos) == 0 or fundos[0].y >= 0:
            fundo = Fundo(0, -2000)
            fundos.append(fundo)

        for i in range(len(fundos)):
            fundos[i].y += velocidade/2
            tela.blit(imagem_fundo, (fundos[i].x, fundos[i].y))

        if len(fundos) > 2:
            del fundos[0]

        # Atribuir pontuacao ao longo do tempo
        if tempo % 14 == 0:
            pontos += 1

        # barra de combustivel
        dt = clock.tick(60) / 1000
        fuel_bar.update(dt)

        # Captura o estado das teclas
        teclas = pygame.key.get_pressed()

        # Movimento do avião
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d] :
            aviao.x += 6
            if aviao.x > 539:
                aviao.x = 539

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a] :
            aviao.x -= 6
            if aviao.x < -20:
                aviao.x = -20

        if teclas[pygame.K_UP] or teclas[pygame.K_w] :
            aviao.y -= 6
            if aviao.y < 35:
                aviao.y = 35

        if teclas[pygame.K_DOWN] or teclas[pygame.K_s] :
            aviao.y += 6
            if aviao.y > 650:
                aviao.y = 650

        # barra de combustivel
        dt = clock.tick(60) / 1000
        fuel_bar.update(dt)

        # Controle de disparo
        agora = pygame.time.get_ticks()
        if teclas[pygame.K_SPACE] and (agora - ultimo_tiro > intervalo_tiro):
            disparo_sound.play()
            nova_bala = Bullet(aviao.x + imagem_aviao.get_width() // 2 - 2, aviao.y)
            balas.append(nova_bala)
            ultimo_tiro = agora

        # Criar novos inimigos
        if tempo % 200 == 0 and fim >= 20:
            fim -= 2
        if randint(1, fim) == 10:
            if randint(1, 3) == 3:
                if pontos > 500:
                    x_random = random.randint(0, tamanho_tela[0] - imagem_nave3.get_width())
                    novo_inimigo = Inimigos(x_random, 35, 3, 5)
                    inimigos.append(novo_inimigo)
                    ultimo_inimigo = agora
                else:
                    x_random = random.randint(0, tamanho_tela[0] - imagem_nave2.get_width())
                    novo_inimigo = Inimigos(x_random, 35, 2, 3)
                    inimigos.append(novo_inimigo)
                    ultimo_inimigo = agora
                
            else:
                x_random = random.randint(0, tamanho_tela[0] - imagem_nave1.get_width())
                novo_inimigo = Inimigos(x_random, 35, 1)
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

        

        # Colisão bullets com inimigo
        for bala in balas[:]:
            bala_rect = pygame.Rect(bala.x, bala.y, 5, 10)
            for inimigo in inimigos[:]:
                if inimigo.tipo == 1:
                    inimigo_rect = pygame.Rect(inimigo.x, inimigo.y, imagem_nave1.get_width(), imagem_nave1.get_height())
                    if bala_rect.colliderect(inimigo_rect):
                        inimigo.vida -= 1
                        if inimigo.vida <= 0:
                            pontos += 50
                            inimigos.remove(inimigo)
                        if bala in balas:
                            balas.remove(bala)
                elif inimigo.tipo == 2:
                    inimigo_rect = pygame.Rect(inimigo.x, inimigo.y, imagem_nave2.get_width(), imagem_nave2.get_height())
                    if bala_rect.colliderect(inimigo_rect):
                        inimigo.vida -= 1
                        if inimigo.vida <= 0:
                            pontos += 100
                            inimigos.remove(inimigo)
                        if bala in balas:
                            balas.remove(bala)
                elif inimigo.tipo == 3:
                    inimigo_rect = pygame.Rect(inimigo.x, inimigo.y, imagem_nave3.get_width(), imagem_nave3.get_height())
                    if bala_rect.colliderect(inimigo_rect):
                        inimigo.vida -= 1
                        if inimigo.vida <= 0:
                            pontos += 500
                            inimigos.remove(inimigo)
                        if bala in balas:
                            balas.remove(bala)

        # Colisão combustivel com o aviao
        for index in range(len(fuels)):
            combustivel_rect = pygame.Rect(fuels[index].x, fuels[index].y, 38, 38)
            aviao_rect = pygame.Rect(aviao.x, aviao.y, imagem_aviao.get_width(), imagem_aviao.get_height())
            if aviao_rect.colliderect(combustivel_rect):
                fuel_bar.pegou_combustivel()
                del fuels[index]
                combustivel_sound.play()
                break

        # Colisao inimigos com o aviao
        for index in range(len(inimigos)):
            if inimigos[index].tipo == 1:
                inimigo_rect = pygame.Rect(inimigos[index].x, inimigos[index].y, imagem_nave1.get_width(), imagem_nave1.get_height())
                aviao_rect = pygame.Rect(aviao.x, aviao.y, imagem_aviao.get_width(), imagem_aviao.get_height())
                if aviao_rect.colliderect(inimigo_rect):
                    aviao.morreu = True
            elif inimigos[index].tipo == 2:
                inimigo_rect = pygame.Rect(inimigos[index].x, inimigos[index].y, imagem_nave2.get_width(), imagem_nave2.get_height())
                aviao_rect = pygame.Rect(aviao.x, aviao.y, imagem_aviao.get_width(), imagem_aviao.get_height())
                if aviao_rect.colliderect(inimigo_rect):
                    aviao.morreu = True
            elif inimigos[index].tipo == 3:
                inimigo_rect = pygame.Rect(inimigos[index].x, inimigos[index].y, imagem_nave3.get_width(), imagem_nave3.get_height())
                aviao_rect = pygame.Rect(aviao.x, aviao.y, imagem_aviao.get_width(), imagem_aviao.get_height())
                if aviao_rect.colliderect(inimigo_rect):
                    aviao.morreu = True

        if fuel_bar.fuel <= 0:
            aviao.morreu = True

        # Desenha elementos na tela

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

        # Desenhar inimigos
        for inimigo in inimigos:
            if inimigo.tipo == 1:
                tela.blit(imagem_nave1, (inimigo.x, inimigo.y))
            elif inimigo.tipo == 2:
                tela.blit(imagem_nave2, (inimigo.x, inimigo.y))
            elif inimigo.tipo == 3:
                tela.blit(imagem_nave3, (inimigo.x, inimigo.y))
            
            

        # Desenha e atualiza balas
        for bala in balas[:]:
            bala.mover()
            if bala.fora_da_tela():
                balas.remove(bala)
            else:
                bala.desenhar(tela)

        # Revome as balas do vetor
        for index in range(len(balas)):
            if balas[index].y <= -10:
                del balas[index]
        fuel_bar.draw(tela)
        tela.blit(texto_formatado, (525, 20))  # Pontuação

        # Atualiza a tela
        pygame.display.update()

        # Controla o FPS
        clock.tick(fps)

        if aviao.morreu:
            while True:
                if morreu(tela, tamanho_tela, cor_branco, pontos):
                    break
