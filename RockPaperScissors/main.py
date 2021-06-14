import random

def play():
    user_choice = input("What is Your choice ? \n 'r' for rock, 'p' for paper, 's' for scissors : ").lower()
    computer_choice = random.choice(['r','p','s'])
    if computer_choice == user_choice:
        return 'It\'s a tie'

    if is_win(computer_choice, user_choice):
        return "You Won!"
    
    return "You lost!"

def is_win(opponent, player):
    if (player == 'r' and opponent == "s") or (player == 'p' and opponent == "r") or (player == 's' and opponent == "p"):
        return True

if __name__ == "__main__":
    print(play())