import pygame
import time


class AviaoLocalizacao:
    def __init__(self, x, y):
        AviaoLocalizacao.x = x
        AviaoLocalizacao.y = y


# Iniciando o pygame
pygame.init()

# Essa cor é no padrao RGB
cor = (255, 255, 255)

tamanho_tela = (640, 480)

tela = pygame.display.set_mode(tamanho_tela)
tela.fill(cor)
pygame.display.update()

aviao_localizacao = AviaoLocalizacao(155, 125)
imagem_aviao = pygame.image.load('aviao.png').convert_alpha()

tela.blit(imagem_aviao, (aviao_localizacao.x, aviao_localizacao.y))

pygame.display.update()

time.sleep(50)
print('River Raid')

pygame.quit()
