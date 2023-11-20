import random

MODE = 0
def guess_number():
    number = random.randint(1, 100)
    return number

def mode(MODE):
    if MODE == "easy":
        return f"You have {life_counter(MODE)+1} attemps remaining to guess the number."

    elif MODE == "hard":
        return f"You have {life_counter(MODE)+1} attemps remaining to guess the number."

    else:
        return "wrong answer for mode selection please restart again"

def life_counter(MODE):
    if MODE == "hard":
        return 4
    elif MODE == "easy":
        return 9

def Play_again():
    play_again = input("\nDo you want to play again? Type 'yes' or 'no': ")
    if play_again == "no":
        return "Bye!"
    elif play_again == "yes":
        return "yes"
    
      
while True:
    Guess_number = guess_number()
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100")
    MODE = input("Choose difficulty. Type 'easy' or 'hard': ") 
    print(mode(MODE))
    guess = int(input("\nMake a guess: "))
    life = life_counter(MODE)
    while(guess != Guess_number): 
        if life == 0:
            print(f"\nGame over you finished all of your attemps.\nCorrect answer was '{Guess_number}'")
            break
        if guess < Guess_number:
            print("Too low. \nGuess again.")
            life -= 1
            print(f"\nYou have {life+1} attemps remaining to guess the number.")
            guess = int(input("Guess again: "))
        if guess > Guess_number:
            print("Too high. \nGuess again.")
            life -= 1
            print(f"\nYou have {life+1} attemps remaining to guess the number.")
            guess = int(input("Guess again: "))
    if guess == Guess_number:
        print("Perfect, you guessed correct.")
    if Play_again() == "Bye!":
        print("Bye!")
        break
