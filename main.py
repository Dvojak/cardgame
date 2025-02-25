import random
from player import Player
from card import Card
from game import game_loop

# Vytvoření balíčku karet pro oba hráče
deck1 = [Card("Goblin", 1, 2, 1), Card("Ogre", 3, 4, 4)] * 5
deck2 = [Card("Knight", 2, 3, 2), Card("Dragon", 5, 6, 5)] * 5
random.shuffle(deck1)
random.shuffle(deck2)

# Vytvoření hráčů
player1 = Player("Hráč 1", deck1)
player2 = Player("Hráč 2", deck2)

# Spuštění hry
if __name__ == "__main__":
    game_loop(player1, player2)
