from player import Player

def game_loop(player1, player2):
    turn = 1
    while player1.health > 0 and player2.health > 0:
        print(f"\n=== Tah {turn} ===")
        current_player = player1 if turn % 2 == 1 else player2
        # Obnova many (max 10)

        current_player.mana = min(turn, 10)
        print(f"{current_player.name} má {current_player.mana} many.")

        # Líznutí karty
        current_player.draw_card()
        print(f"Draw {current_player.name}: {current_player.hand}")
        
        print("\n=== Tvůj board ===")
        for i,card in enumerate(current_player.board):
                print(f"{i}:{card}")

        print("\n=== Tvoje ruka ===")
        for i,card in enumerate(current_player.hand):
            print(f"{i}: {card}")
        choice = input("Zadej index karty, kterou chceš zahrát, jinak dej enter: ")
        if choice == "":
            pass
        if choice.isdigit():
            choice = int(choice)
            current_player.play_card(choice)
     




        turn += 1

        input("Stiskni Enter pro další tah...")  # Pauza mezi tahy

    print("Konec hry!")

