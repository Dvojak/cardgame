import pygame


class Card:
    def __init__(self, name, cost, attack=0, health=0,photo="card_template"):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.photo = photo
        self.can_attack = True
        self.image = pygame.image.load(f"images/{self.photo}.png")
        
        self.x = 0  # Výchozí pozice, nastaví se při vykreslení
        self.y = 0
        self.width = 100
        self.height = 150

    def draw(self, screen, x, y, font):
        self.x, self.y = x, y  # Uložíme pozici

        pygame.draw.rect(screen, (200, 200, 200), (x, y, self.width, self.height), border_radius=10)
        screen.blit(self.image, (x, y))

        name_text = font.render(self.name, True, (0, 0, 0))
        screen.blit(name_text, (x + 15, y + 5))

        mana_text = font.render(str(self.cost), True, (0, 0, 0))
        screen.blit(mana_text, (x + 5, y + 5))

        attack_text = font.render(str(self.attack), True, (0, 0, 0))
        screen.blit(attack_text, (x + 75, y + 125))

        health_text = font.render(str(self.health), True, (0, 0, 0))
        screen.blit(health_text, (x + 5, y + 125))

    def was_clicked(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height


    def __repr__(self):
        return f"{self.name} (Mana: {self.cost}, Atk: {self.attack}, HP: {self.health})"

class Effect:
        def __init__(self, name, trigger, action, value):
            self.name = name         # Jméno efektu
            self.trigger = trigger   # Kdy se aktivuje (např. "play", "attack")
            self.action = action     # Co dělá (např. "damage", "buff", "draw","heal")
            self.value = value       # Počet poškození, buff, draw, heal atd.
        
        def activate_effect(self, target = ""):
            from player import Player

            if self.action == "damage":
                pass
            elif self.action == "buff":
                
                pass
            elif self.action == "draw":
                Player.draw_card() * self.value
                pass
            elif self.action == "heal": 
                pass
