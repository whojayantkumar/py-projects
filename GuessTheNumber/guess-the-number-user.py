import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? : ").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1 
    print(f"Yay, congrats. You have guessed the number {guess} correctly.")

if __name__ == "__main__":
    print("Hello Guys, Think a number between 1 to 1000")
    computer_guess(1000)