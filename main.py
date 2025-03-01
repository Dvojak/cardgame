import pygame
import random
from player import Player
from card import Card
import graphics  # Import grafických funkcí

# Vytvoření balíčku karet pro oba hráče
deck1 = [Card("Goblin", 1, 2, 1), Card("Ogre", 3, 4, 4)] * 5
deck2 = [Card("Knight", 2, 3, 2), Card("Dragon", 5, 6, 5)] * 5
random.shuffle(deck1)
random.shuffle(deck2)

# Vytvoření hráčů
player1 = Player("Hráč 1", deck1)
player2 = Player("Hráč 2", deck2)

# Hlavní smyčka hry
running = True
turn = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vyplnění pozadí bílou barvou
    graphics.screen.fill(graphics.WHITE)

    # Vykreslení informací o hráčích
    graphics.draw_player_info(player1, turn)
    graphics.draw_player_info(player2, turn)
    
    # Vykreslení boardu
    graphics.draw_board(player1)
    graphics.draw_board(player2)

    # Ukázat, kdo má aktuálně tah
    graphics.draw_turn(turn)

    # Aktualizace okna
    graphics.update_screen()

    # Předání tahu
    turn += 1

# Ukončení Pygame
pygame.quit()
