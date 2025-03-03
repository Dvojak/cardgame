import pygame
from player import Player
from card import Card

def game_loop(player1, player2):
    round = 1
    turn = 1
    running = True
    pass_counter = 0
    selected_card = None 
    WIDTH, HEIGHT = 1280, 600

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

        screen.blit(top_text, (50, 10))  # Protivník nahoře
        screen.blit(bottom_text, (50, 550))  # Hráč na tahu dole

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
            x = 305 + i * 120
            y = 450  # Ještě níž než board
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
                        break
            elif event.type == pygame.MOUSEBUTTONDOWN:  
               mouse_x, mouse_y = pygame.mouse.get_pos()
                # 1) Nejprve zkusíme vyložit kartu
               for i, card in enumerate(bottom_player.hand):
                    if card.was_clicked(mouse_x, mouse_y):
                        if bottom_player.mana >= card.cost:  # Má dost many?
                            bottom_player.play_card(i)
                            print(f"{bottom_player.name} vyložil kartu {card.name}")
                            pass_counter = 0
                            turn += 1
                            break
                        else:
                            print("Nedostatek many!")
                            

    # 2) Pokud nebyla vyložena karta, zkontrolujeme útok

    # Pokud ještě není vybraná karta k útoku, zkusíme ji vybrat
        if selected_card is None:
            for card in bottom_player.board:
                if card.was_clicked(mouse_x, mouse_y) :
                    selected_card = card
                    print(f"Vybrána karta k útoku: {card.name}")
                    break

    # Pokud už je karta vybraná, pokusíme se zaútočit
        else:
            for card in top_player.board:
                if card.was_clicked(mouse_x, mouse_y):
                    bottom_player.attack_card(bottom_player.board.index(selected_card), card, top_player)
                    selected_card = None  # Reset výběru
                    break
            else:  # Pokud nemá soupeř karty, útok na hráče
                if 50 <= mouse_x <= 250 and 10 <= mouse_y <= 100:  # Klik na horního hráče
                    bottom_player.attack_card(bottom_player.board.index(selected_card), top_player, top_player)
                    selected_card = None



pygame.quit()
