class effect:
        def __init__(self, name, trigger, action, value):
            self.name = name         # Jméno efektu
            self.trigger = trigger   # Kdy se aktivuje (např. "play", "attack")
            self.action = action     # Co dělá (např. "damage", "buff", "draw","heal")
            self.value = value       # Počet poškození, buff, draw, heal atd.
        
        def activate_effect(self):
            if self.action == "damage":
                pass
            elif self.action == "buff":
                pass
            elif self.action == "draw":
                pass
            elif self.action == "heal": 
                pass