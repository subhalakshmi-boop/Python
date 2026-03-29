import random
def roll_dice():
    return random.randint(1, 6)
def play_game():
    print("===== DICE GAME =====")
    print("Player vs Computer\n")
    player_score = 0
    computer_score = 0
    rounds = 5
    for i in range(1, rounds + 1):
        input(f"Round {i} - Press Enter to roll dice...")
        player_roll = roll_dice()
        computer_roll = roll_dice()
        print(f"You rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")
        if player_roll > computer_roll:
            print("You win this round!\n")
            player_score += 1
        elif computer_roll > player_roll:
            print("Computer wins this round!\n")
            computer_score += 1
        else:
            print("It's a tie!\n")
    print("===== FINAL RESULT =====")
    print(f"Your Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    if player_score > computer_score:
        print("You are the Winner!")
    elif computer_score > player_score:
        print("Computer Wins!")
    else:
        print("It's a Draw!")
play_game()
