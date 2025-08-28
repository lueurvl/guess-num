#!usr/bin/env python3

import random

def main():
    while True:
        play_game()
        again = input("You wanna play again? (y/n):").strip().lower()
        if again != 'y':
            print("See ya!")
            break
    
def play_game():
    print("Thinking of a number between 1 and 20")
    secret = random.randint(1, 20)
    limit = input("How many tries you want? (default is 5): ") or 5
    try:
        limit = int(limit)
    except ValueError:
        print("You have entered an invalid value. Using default value (5).")
        limit = 5
    if limit <= 0:
        print("You have mistakenly entered your IQ. Using default value (5).")
        limit = 5
    
    for tries in range (1, limit + 1):
        guess_str = input("Take a guess: ").strip()
        if not guess_str:
            print("Enter a number!")
            continue
        try:
            guess = int(guess_str)
        except ValueError:
            print("You have entered an invalid input. Try again!.")
            continue
        if guess <= 0:
            print("Are you high? I said the number is between 1-20. Try again!?")
            continue

        if guess < secret:
            print("Your guess is lower.")
        elif guess > secret:
            print("Your guess is higher.")
        else:
            print(f"You have won! You guessed my number in {tries} tries.")
            break
    else:
        print(f"You have lost. You used all your tries. The number was {secret}.")

if __name__ == "__main__":
    main()
