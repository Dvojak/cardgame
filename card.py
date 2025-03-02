import pygame


class Card:
    def __init__(self, name, cost, attack=0, health=0):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.can_attack = True 
        self.image = pygame.image.load(f"images/Rehor.png")
    def draw(self, screen, x, y, font):
        # Vykreslení obdélníku pro kartu
        pygame.draw.rect(screen, (200, 200, 200), (x, y, 100, 150), border_radius=10)
        
        # Vykreslení obrázku
        screen.blit(self.image, (x + 10, y + 30))
        
        # Vykreslení jména karty
        name_text = font.render(self.name, True, (0, 0, 0))
        screen.blit(name_text, (x + 5, y + 5))
        
        # Vykreslení many vlevo nahoře
        mana_text = font.render(str(self.cost), True, (0, 0, 255))
        screen.blit(mana_text, (x + 5, y + 5))
        
        # Vykreslení síly vpravo dole
        attack_text = font.render(str(self.attack), True, (255, 0, 0))
        screen.blit(attack_text, (x + 75, y + 125))
        
        # Vykreslení životů vlevo dole
        health_text = font.render(str(self.health), True, (0, 255, 0))
        screen.blit(health_text, (x + 5, y + 125))
    

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
