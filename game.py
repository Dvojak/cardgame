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

        # Líznutí karty
        current_player.draw_card()
        print(f"Draw {current_player.name}: {current_player.hand}")
        
        print("\n=== Soupeřův board ===")
        for i,card in enumerate(opponent.board):
                print(f"{i}:{card}")

        print("\n=== Tvůj board ===")
        for i,card in enumerate(current_player.board):
                print(f"{i}:{card}")

        print("\n=== Tvoje ruka ===")
        for i,card in enumerate(current_player.hand):
            print(f"{i}: {card}")

        Which = input("1. Vylož kartu na board\n2. Zaútočit s kartou na boardu\n") 
        if Which == "1":
            choice = input("Zadej index karty, kterou chceš vyložit na board, jinak dej enter: ")
            if choice == "":
                pass
            if choice.isdigit():
                choice = (choice)
                current_player.play_card(choice)   
        elif Which == "2":
            choice = input("Zadej index karty, kterou zaútočíš, jinak dej enter: ")
            if choice == "":
                pass
            if choice.isdigit():
                attack = input("Zadej index karty, na kterou zaútočíš, jinak dej enter: ")
                if attack == "":
                    pass
                if attack.isdigit():
                     current_player.attack_card(int(choice), int(attack))





        turn += 1

        input("Stiskni Enter pro další tah...")  # Pauza mezi tahy

    print("Konec hry!")

