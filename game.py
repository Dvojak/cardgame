from player import Player

def game_loop(player1, player2):
    round = 1
    while player1.health > 0 and player2.health > 0:
        print(f"\n=== Kolo {round} ===")
        pass_counter = 0  # Počítá pasování obou hráčů

        # Obnova many (max 10)
        player1.mana = min(round, 10)
        player2.mana = min(round, 10)

        # Líznutí karty
        player1.draw_card()
        player2.draw_card()
        
        turn = 1
        while pass_counter < 2:  # Kolo pokračuje, dokud oba hráči nepasují
            current_player = player1 if turn % 2 == 1 else player2
            opponent = player2 if current_player == player1 else player1
            print(f"\n=== Tah {turn} ===")
            print(f"{current_player.name} má {current_player.mana} many a {current_player.health} HP.")

            print("\n=== Soupeřův board ===")
            for i, card in enumerate(opponent.board, start=1):
                print(f"{i}: {card}")

            print("\n=== Tvůj board ===")
            for i, card in enumerate(current_player.board, start=1):
                print(f"{i}: {card}")

            print("\n=== Tvoje ruka ===")
            for i, card in enumerate(current_player.hand, start=1):
                print(f"{i}: {card}")

            print("\n=== Tvoje akce ===")
            Which = input("1. Vylož kartu (předá tah)\n2. Zaútočit\nEnter pro pasování tahu\n") 

            if Which == "1":
                choice = input("Zadej index karty k vyložení (nebo enter pro zpět): ")
                if choice.isdigit():
                    choice = int(choice) - 1
                    current_player.play_card(choice)
                    print(f"\n{current_player.name} vyložil kartu!")
                    input("\nEnter pro pokračování...")  # Pauza, aby bylo vidět, co se stalo
                    pass_counter = 0  # Resetuje pasování
                    turn += 1  # Předá tah soupeři
                    continue  

            elif Which == "2":
                choice = int(input("Zadej index karty, kterou útočíš: ")) - 1
                attack = int(input("Zadej index cíle útoku (0 pro hráče): "))  

                if attack == 0 and opponent.board == []:
                    target = opponent  
                elif 1 <= attack <= len(opponent.board):
                    target = opponent.board[attack - 1]  
                else:
                    print("Neplatný cíl!")
                    target = None  

                if target:
                    current_player.attack_card(choice, target, opponent, attack - 1)  
                    print(f"\n{current_player.name} zaútočil na {target}!")
                    input("\nEnter pro pokračování...")  # Pauza po útoku
                    pass_counter = 0  # Reset pasování
                continue  # Po útoku hráč může hrát dál

            elif Which == "":  # Hráč pasuje
                pass_counter += 1  
                turn += 1  # Předá tah soupeři
                print(f"{current_player.name} pasuje.")
                input("\nEnter pro pokračování...")  # Pauza po pasování

        round += 1  # Pokud oba pasovali, začne nové kolo





    print("Konec hry!")

