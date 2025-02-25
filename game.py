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
        print(f"Ruka {current_player.name}: {current_player.hand}")

        # Simulace hraní karty (pokud nějakou má)
        if current_player.hand:
            current_player.play_card(0)  # Hraje první kartu v ruce

        turn += 1

    print("Konec hry!")
