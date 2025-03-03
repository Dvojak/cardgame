import pygame
from player import Player
from card import Card

def game_loop(player1, player2):
    round = 1
    turn = 1
    running = True
    pass_counter = 0
    WIDTH, HEIGHT = 800, 600

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Karetní hra")
    font = pygame.font.Font(None, 36)

    while running:
        screen.fill((0, 128, 0))  # Zelené pozadí

        # Dynamicky určíme, kdo je hráč dole a kdo nahoře
        bottom_player = player1 if turn % 2 == 1 else player2
        top_player = player2 if bottom_player == player1 else player1

        # Zobrazení informací o hráčích (aktuální hráč dole, protivník nahoře)
        bottom_text = font.render(f"{bottom_player.name}: {bottom_player.health} HP, {bottom_player.mana} Mana", True, (255, 255, 255))
        top_text = font.render(f"{top_player.name}: {top_player.health} HP, {top_player.mana} Mana", True, (255, 255, 255))

        screen.blit(top_text, (50, 50))  # Protivník nahoře
        screen.blit(bottom_text, (50, 500))  # Hráč na tahu dole

        # Vykreslení karet hráče nahoře
        for i, card in enumerate(top_player.board):
            x = 50 + i * 120
            y = 100  # Výš než předtím, protože je to horní hráč
            card.draw(screen, x, y, font)

        # Vykreslení karet hráče dole (aktuálního hráče na tahu)
        for i, card in enumerate(bottom_player.board):
            x = 50 + i * 120
            y = 300  # Níž než protivník
            card.draw(screen, x, y, font)

        # Vykreslení karet v ruce hráče na tahu (dole)
        for i, card in enumerate(bottom_player.hand):
            x = 50 + i * 120
            y = 350  # Ještě níž než board
            card.draw(screen, x, y, font)

        pygame.display.flip()

        # Herní smyčka - události
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass_counter += 1
                    turn += 1
                    if pass_counter >= 2:
                        round += 1
                        pass_counter = 0
                        bottom_player.mana = min(round, 10)
                        top_player.mana = min(round, 10)
                        bottom_player.draw_card()
                        top_player.draw_card()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Kliknutí myší
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i,card in enumerate(bottom_player.hand):
                    if card.was_clicked(mouse_x, mouse_y):
                        if bottom_player.mana >= card.cost:  # Má dost many?
                            bottom_player.play_card(i)
                            print(f"{bottom_player.name} vyložil kartu {card.name}")
                        else:
                            print("Nedostatek many!")


pygame.quit()
