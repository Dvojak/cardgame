import random
from player import Player
from card import Card
from game import game_loop

# Vytvoření balíčku karet pro oba hráče
deck1 = [Card("Goblin", 1, 2, 1,"goblin"), Card("Ogre", 3, 4, 4,"ogre"), Card("Elf", 2, 3, 2,"long_legs"), Card("Troll", 4, 5, 5,"troll")]
deck2 = [Card("Knight", 2, 3, 2,"knight"), Card("Dragon", 5, 6, 5,"dragon"), Card("Wizard", 4, 5, 3,"wizard"), Card("Archer", 3, 4, 2,"archer")]
random.shuffle(deck1)
random.shuffle(deck2)

# Vytvoření hráčů
player1 = Player("Hráč 1", deck1)
player2 = Player("Hráč 2", deck2)

# Spuštění hry
if __name__ == "__main__":
    game_loop(player1, player2)