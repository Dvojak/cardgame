import pygame

# Inicializace Pygame
pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Karetní hra")

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_board(player):
    """Vykreslí board hráče."""
    y_offset = 100
    for card in player.board:
        pygame.draw.rect(screen, (0, 0, 255), (100, y_offset, 100, 150))  # Karta je obdélník
        y_offset += 160  # Posun pro další kartu
        font = pygame.font.Font(None, 36)
        text = font.render(card.name, True, BLACK)
        screen.blit(text, (110, y_offset - 140))

def draw_player_info(player, turn):
    """Vykreslí informace o hráči."""
    font = pygame.font.Font(None, 36)
    text = font.render(f"{player.name} (Mana: {player.mana}, HP: {player.health})", True, BLACK)
    screen.blit(text, (10, 10))

def draw_turn(turn):
    """Vykreslí text pro aktuální kolo."""
    font = pygame.font.Font(None, 48)
    text = font.render(f"Turn: {turn}", True, BLACK)
    screen.blit(text, (WIDTH // 2 - 100, 30))

def update_screen():
    """Aktualizuje okno a čeká na další akce."""
    pygame.display.flip()
    pygame.time.wait(1000)  # Čekání mezi tazemi
