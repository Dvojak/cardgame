import random
from card import Card

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.health = 30
        self.mana = 1
        self.deck = deck
        self.hand = []
        self.board = []

    def draw_card(self):
        if self.deck:
            self.hand.append(self.deck.pop(0))
        else:
            print(f"{self.name} už nemá karty v balíčku!")

    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            card = self.hand[card_index]
            if card.cost <= self.mana:
                self.mana -= card.cost
                self.board.append(self.hand.pop(card_index))
                print(f"{self.name} zahrál {card.name}.")
            else:
                print(f"Nedostatek many pro {card.name}!")
        else:
            print("Neplatný index karty!") 
    def attack_card(self, card_index, target,opponent,who):
     attacker = self.board[card_index]  # Útočník
     if isinstance(target, Card):  # Cíl je karta
        target_index = opponent.board[who]  # Cíl útoku
        target.health -= attacker.attack
        attacker.health -= target.attack  # Protivýpad
        print(f"{attacker.name} útočí na {target.name}!")

        # Odstranění mrtvých karet
        if target.health <= 0:
            opponent.board.remove(target_index)
            print(f"{target.name} byla zničena!")

        if attacker.health <= 0:
            self.board.remove(attacker)
            print(f"{attacker.name} byla zničena!")

     elif isinstance(target, Player):  # Cíl je hráč
        target.health -= attacker.attack
        print(f"{attacker.name} útočí na hráče za {attacker.attack} DMG!")
        Card.can_attack = False 
          
    def __repr__(self):
        return f"{self.name} (HP: {self.health}, Mana: {self.mana})"
