############### Blackjack Project #####################

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

random_cards_pc = []
random_card_selection_pc_1 = random.choice(cards)
random_card_selection_pc_2 = random.choice(cards)
random_cards_pc.append(random_card_selection_pc_1)
random_cards_pc.append(random_card_selection_pc_2)
sum_of_cards_pc = 0
print(random_card_selection_pc_2)

random_cards = []
random_card_selection_1 = random.choice(cards)
random_card_selection_2 = random.choice(cards)
random_cards.append(random_card_selection_1)
random_cards.append(random_card_selection_2)
sum_of_cards = 0

sum_of_cards = random_card_selection_1 + random_card_selection_2

if random_card_selection_1 + random_card_selection_2 == 21:
    print("Safak, BlackJack, you won.")

print(random_cards)

if sum_of_cards == 21 and sum_of_cards_pc == 21:
    print("Draw, Double blackjack!!!")
    
more_card = "no"
    
if sum_of_cards > 21:
    for i in range(len(random_cards)):
        if random_cards[i] == cards[0]:
            if sum_of_cards >= 22:
                random_cards[i] = random_cards[i] - 10
                sum_of_cards = sum_of_cards - 10
                print(random_cards[i])
                print(sum_of_cards)

if sum_of_cards < 21:
    more_card = input("Do you want card? (yes/no): ")

while more_card == "yes":
    random_card_selection_more = random.choice(cards)
    random_cards.append(random_card_selection_more)
    print(f"random cards{random_cards}")
    sum_of_cards += random_card_selection_more
    
    for i in range(len(random_cards)):
        if random_cards[i] == cards[0]:
            if sum_of_cards >= 22:
                random_cards[i] = random_cards[i] - 10
                sum_of_cards = sum_of_cards - 10
                print(random_cards[i])
                print(sum_of_cards)
            elif sum_of_cards >= 22:
                more_card = "no"
        
    if sum_of_cards == 21:
        print("Safak, BlackJack, you won.")
        more_card_pc = "no"
        break
    if sum_of_cards < 21:
        more_card = input("Do you want card? (yes/no): ")
    
    if more_card == "no":
        more_card = "no"
        print(f"Safak: {random_cards}")

sum_of_cards_pc = random_card_selection_pc_1 + random_card_selection_pc_2

more_card_pc = "no"
if sum_of_cards_pc < sum_of_cards:
    if sum_of_cards_pc < 22:
        if sum_of_cards < 22:
            more_card_pc = "yes"
            
        elif sum_of_cards == 21:
            more_card_pc = "no"
    
elif sum_of_cards == sum_of_cards_pc:
    print("Draww eşit")
    
while more_card_pc == "yes":
    if random_card_selection_pc_1 + random_card_selection_pc_2 == 21:
        print("PC, BlackJack, PC won.")
        break
    
    if sum_of_cards < sum_of_cards_pc:    
        if sum_of_cards_pc < 22:
            print("PC won!")
            break
        
    if sum_of_cards_pc > 21:
        more_card_pc = "no"
        break
    
    random_card_selection_pc_more = random.choice(cards)
    random_cards_pc.append(random_card_selection_pc_more)
    sum_of_cards_pc += random_card_selection_pc_more
    
    for i in range(len(random_cards_pc)):
        if random_cards_pc[i] == cards[0]:
            if sum_of_cards_pc >= 22:
                random_cards_pc[i] = random_cards_pc[i] - 10
                sum_of_cards_pc = sum_of_cards_pc - 10

    if sum_of_cards_pc >= 22:
        print("PC lost this hand")
        break
    
    if sum_of_cards_pc == 21:
        print("PC, BlackJack, PC won.")
        break
    
    if random_card_selection_pc_1 + random_card_selection_pc_2 <= random_card_selection_1 + random_card_selection_2:
        if random_card_selection_pc_1 + random_card_selection_pc_2 > 21:
            more_card_pc = "no"
        elif random_card_selection_pc_1 + random_card_selection_pc_2 < 21:
            more_card_pc = "yes"
    
    elif random_card_selection_pc_1 + random_card_selection_pc_2 <= random_card_selection_1 + random_card_selection_2:
        more_card_pc = "no"
        
if sum_of_cards > sum_of_cards_pc:
    if sum_of_cards <= 21:
        print("Safak you won!")
        
if sum_of_cards >= 21:
        print("Safak busted!, you lost!")
        more_card = "no"
        
print(f"PC: {random_cards_pc}")
