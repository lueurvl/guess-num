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
    print("Thinkin of a number bw 1 and 20")
    secret = random.randint(1, 20)
    limit = input("How many fuckin tries do you want to guess? (default is 5): ") or 5
    try:
        limit = int(limit)
    except ValueError:
        print("This is fuckin invalid, are you high bitch? Whatever, idc, using default.")
        limit = 5
    if limit <= 0:
        print("I didn't ask you to enter your IQ, are you on coke? Whatever bitch, idc, using default.")
        limit = 5
    
    for tries in range (1, limit + 1):
        guess_str = input("Take a guess motherfucker: ").strip()
        if not guess_str:
            print("Enter a number, retard!")
            continue
        try:
            guess = int(guess_str)
        except ValueError:
            print("Thats not a fuckin number try again bae.")
            continue
        if guess <= 0:
            print("Why the fuck are you entering your IQ?")
            continue

        if guess < secret:
            print("Your guess is LOW.")
        elif guess > secret:
            print("Your guess is HIGH.")
        else:
            print(f"Fuck you, you won! You guessed my number in {tries} fuckin tries.")
            break
    else:
        print(f"You lost bitch, you used all your tries. The number was {secret}.")

if __name__ == "__main__":
    main()