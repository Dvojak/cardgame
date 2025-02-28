from player import Player

def game_loop(player1, player2):
    turn = 1
    while player1.health > 0 and player2.health > 0:
        print(f"\n=== Tah {turn} ===")

        current_player = player1 if turn % 2 == 1 else player2
        opponent = player2 if current_player == player1 else player1
        # Obnova many (max 10)

        current_player.mana = min(turn, 10)
        print(f"{current_player.name} má {current_player.mana} many.")
        print(f"{current_player.name}: má {current_player.health} HP")
        print("\n=== Líznutí karty ===")
        # Líznutí karty
        current_player.draw_card()
        
        print("\n=== Soupeřův board ===")
        for i,card in enumerate(opponent.board, start=1):
                print(f"{i}:{card}")

        print("\n=== Tvůj board ===")
        for i,card in enumerate(current_player.board, start=1):
                print(f"{i}:{card}")

        print("\n=== Tvoje ruka ===")
        for i,card in enumerate(current_player.hand, start=1):
            print(f"{i}: {card}")
        print("\n=== Tvoje akce ===")
        Which = input("1. Vylož kartu na board\n2. Zaútočit s kartou na boardu\n") 
        if Which == "1":
            choice = input("Zadej index karty, kterou chceš vyložit na board, jinak dej enter: ")
            if choice == "":
                pass
            if choice.isdigit():
                choice = int(choice) - 1
                current_player.play_card(choice)
        elif Which == "2":
           choice = int(input("Zadej index karty, kterou zaútočíš: ")) - 1  # Převedení na index
           attack = int(input("Zadej index cíle útoku (0 pro hráče): "))  # Cíl útoku

           if attack == 0 and opponent.board == []:
            target = opponent  # Útok na hráče
           elif 1 <= attack <= len(opponent.board):
            target = opponent.board[attack - 1]  # Útok na kartu
           else:
             print("Neplatný cíl!")
             target = None  # Neplatná volba

           if target:
             current_player.attack_card(choice, target,opponent,int(attack)-1)  





        turn += 1

        input("Stiskni Enter pro další tah...")  # Pauza mezi tahy

    print("Konec hry!")

