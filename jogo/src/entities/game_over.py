import pygame
import sys
import os


def morreu(tela, tamanho_tela, cor_branco, pontos):
    fonte_opcoes = pygame.font.SysFont('space', 50, True, False)
    fonte_pontos = pygame.font.SysFont('space', 40, True, False)  # Fonte para os pontos
    menu_ativo = True

    imagem_path_game_over = os.path.join(os.getcwd(), '..', 'assets', 'images', 'game_over.png')
    imagem_menu = pygame.image.load(imagem_path_game_over).convert_alpha()

    while menu_ativo:
        tela.fill(cor_branco)
        tela.blit(imagem_menu, (0, 0))

        botao_menu = fonte_opcoes.render("Voltar ao menu", True, cor_branco)
        tela.blit(botao_menu, (tamanho_tela[0] // 2 - botao_menu.get_width() // 2, 450))

        # Renderizando os pontos na tela
        texto_pontos = fonte_pontos.render(f"Pontos: {pontos:03}", True, cor_branco)
        tela.blit(texto_pontos, (tamanho_tela[0] // 2 - texto_pontos.get_width() // 2, 350))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if (tamanho_tela[0] // 2 - botao_menu.get_width() // 2 <= mouse_pos[0] <= tamanho_tela[
                    0] // 2 + botao_menu.get_width() // 2 and
                        450 <= mouse_pos[1] <= 450 + botao_menu.get_height()):
                    return True

        pygame.display.update()
