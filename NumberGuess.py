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

def main():
    Guess_number = guess_number()
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100")
    MODE = input("Choose difficulty. Type 'easy' or 'hard': ") 
    print(mode(MODE))
    guess = int(input("Make a guess: "))
    life = life_counter(MODE)
    while(guess != Guess_number):  
        if life == 0:
            print(f"Game over you finished all of your attemps.\nCorrect answer was '{Guess_number}'")
            break
        if guess < Guess_number:
            print("Too low. \n Guess again.")
            life -= 1
            guess = int(input("Guess again: "))
        if guess > Guess_number:
            print("Too high. \n Guess again.")
            life -= 1
            guess = int(input("Guess again: "))
    if guess == Guess_number:
        print("Perfect, you guessed correct.")
        
main()
