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

    def attack_card(self, card_index, target, opponent):
        attacker = self.board[card_index]

        if not attacker.can_attack:
            print(f"{attacker.name} už tento tah útočila!")
            return

        if isinstance(target, Card):
            target.health -= attacker.attack
            attacker.health -= target.attack
            print(f"{attacker.name} útočí na {target.name}!")

            if target.health <= 0:
                opponent.board.remove(target)
                print(f"{target.name} byla zničena!")

            if attacker.health <= 0:
                self.board.remove(attacker)
                print(f"{attacker.name} byla zničena!")

        elif isinstance(target, Player):
            target.health -= attacker.attack
            print(f"{attacker.name} útočí na hráče za {attacker.attack} DMG!")

        attacker.can_attack = False  # Zabránění opakovanému útoku

    def get_hand_info(self):
        return [str(card) for card in self.hand]

    def get_board_info(self):
        return [str(card) for card in self.board]

    def __repr__(self):
        return f"{self.name} (HP: {self.health}, Mana: {self.mana})"
