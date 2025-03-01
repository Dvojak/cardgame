


class Card:
    def __init__(self, name, cost, attack=0, health=0):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.can_attack = True 

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
