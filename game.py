import pygame
from player import Player

def game_loop(player1, player2):
    round = 1
    turn = 1
    running = True
    pass_counter = 0
    WIDTH, HEIGHT = 800, 600
    # Inicializace Pygame
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Karetní hra")
    font = pygame.font.Font(None, 36)  # Výchozí font

    
    while running:
        screen.fill((0, 128, 0))  # Zelené pozadí jako herní stůl
        current_player = player1 if turn % 2 == 1 else player2
        opponent = player2 if current_player == player1 else player1
        
        # Zobrazení informací o hráčích
        player1_text = font.render(f"{player1.name}: {player1.health} HP, {player1.mana} Mana", True, (255, 255, 255))
        player2_text = font.render(f"{player2.name}: {player2.health} HP, {player2.mana} Mana", True, (255, 255, 255))
        screen.blit(player1_text, (50, 50))
        screen.blit(player2_text, (50, 500))
        
        # Vykreslení karet na ruce a boardu (zatím jen jako text)
        for i, card in enumerate(current_player.hand):
            card_text = font.render(f"{card.name} ({card.cost} mana)", True, (255, 255, 255))
            screen.blit(card_text, (50 + i * 100, 400))
        
        for i, card in enumerate(current_player.board):
            card_text = font.render(f"{card.name} {card.attack}/{card.health}", True, (255, 255, 255))
            screen.blit(card_text, (50 + i * 100, 300))
        
        pygame.display.flip()
        # Herní smyčka reagující na události
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
                        player1.mana = min(round, 10)
                        player2.mana = min(round, 10)
                        player1.draw_card()
                        player2.draw_card()
                        
    
    pygame.quit()
