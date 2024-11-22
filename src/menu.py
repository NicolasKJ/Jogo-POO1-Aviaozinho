import pygame
import sys

def exibir_menu(tela, tamanho_tela, cor_branco, cor_preto):
    fonte_menu = pygame.font.SysFont('space', 50, True, False)
    fonte_opcoes = pygame.font.SysFont('space', 40, True, False)
    menu_ativo = True

    while menu_ativo:
        tela.fill(cor_branco)

        titulo = fonte_menu.render("River Raid", True, cor_preto)
        tela.blit(titulo, (tamanho_tela[0] // 2 - titulo.get_width() // 2, 100))

        botao_iniciar = fonte_opcoes.render("Iniciar", True, cor_preto)
        botao_sair = fonte_opcoes.render("Sair", True, cor_preto)

        tela.blit(botao_iniciar, (tamanho_tela[0] // 2 - botao_iniciar.get_width() // 2, 250))
        tela.blit(botao_sair, (tamanho_tela[0] // 2 - botao_sair.get_width() // 2, 350))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if (tamanho_tela[0] // 2 - botao_iniciar.get_width() // 2 <= mouse_pos[0] <= tamanho_tela[0] // 2 + botao_iniciar.get_width() // 2 and
                    250 <= mouse_pos[1] <= 250 + botao_iniciar.get_height()):
                    menu_ativo = False 
                    
                if (tamanho_tela[0] // 2 - botao_sair.get_width() // 2 <= mouse_pos[0] <= tamanho_tela[0] // 2 + botao_sair.get_width() // 2 and
                    350 <= mouse_pos[1] <= 350 + botao_sair.get_height()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
