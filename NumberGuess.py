import random

def guess_number():
    number = random.randint(1, 100)
    return number

def mode(mode):
    if mode == "easy":
        mode == "easy"
        print("You have 10 attemps remaining to guess the number.")
        
    elif mode == "hard":
        mode == "hard"
        print("You have 5 attemps remaining to guess the number.")
        
    else:
        print("wrong answer for mode selection please restart again")
        
        
def attempt(mode):
    if mode == "easy":
        mode == "easy"
        print("You have 10 attemps remaining to guess the number.")
        
    elif mode == "hard":
        mode == "hard"
        print("You have 5 attemps remaining to guess the number.")
        
    else:
        print("wrong answer for mode selection please restart again")
        
def life_counter(mode):
    if mode == "hard":
        return 4
    elif mode == "easy":
        return 9
    

def main():
    Guess_number = guess_number()
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100")
    mode = input("Choose difficulty. Type 'easy' or 'hard': ") 
    guess = int(input("Make a guess: "))
    life = life_counter(mode)
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
