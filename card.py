from effect import Effect


class Card:
    def __init__(self, name, cost, attack=0, health=0):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.can_attack = True 

    def __repr__(self):
        return f"{self.name} (Mana: {self.cost}, Atk: {self.attack}, HP: {self.health})"
