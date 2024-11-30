import pygame
import sys
import os


def exibir_menu(tela, tamanho_tela, cor_branco, cor_preto):
    fonte_opcoes = pygame.font.SysFont('space', 50, True, False)
    menu_ativo = True

    imagem_path_menu = os.path.join(os.getcwd(), '..', 'assets', 'images', 'imagem_menu.png')
    imagem_menu = pygame.image.load(imagem_path_menu).convert_alpha()

    while menu_ativo:
        tela.fill(cor_branco)
        tela.blit(imagem_menu, (0, 0))

        botao_iniciar = fonte_opcoes.render("Iniciar", True, cor_branco)
        botao_sair = fonte_opcoes.render("Sair", True, cor_branco)

        tela.blit(botao_iniciar, (tamanho_tela[0] // 2 - botao_iniciar.get_width() // 2, 350))
        tela.blit(botao_sair, (tamanho_tela[0] // 2 - botao_sair.get_width() // 2, 450))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if (tamanho_tela[0] // 2 - botao_iniciar.get_width() // 2 <= mouse_pos[0] <= tamanho_tela[0] // 2 + botao_iniciar.get_width() // 2 and
                    350 <= mouse_pos[1] <= 350 + botao_iniciar.get_height()):
                    menu_ativo = False 
                    
                if (tamanho_tela[0] // 2 - botao_sair.get_width() // 2 <= mouse_pos[0] <= tamanho_tela[0] // 2 + botao_sair.get_width() // 2 and
                    450 <= mouse_pos[1] <= 450 + botao_sair.get_height()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
