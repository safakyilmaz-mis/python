import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

userName = input("Welcome to BlackJack game, enter your name: ")
def selectCards():
    return [random.choice(cards),random.choice(cards)]

def isBlackJack(userHandTotal,PChandTotal):
    if userHandTotal == 21:
        print(f"{userName}, blackjack, you won!")
    elif PChandTotal == 21:
        print(f"PC, blackjack, you won!")
    
def isBusted(userHandTotal,PChandTotal):
    if userHandTotal > 21 or PChandTotal > 21:
        return True
def elevenToOne(hand):
    if sum(hand) >= 21 and 11 in hand:
        hand[hand.index(11)] = 1

def PC_cardDecision(userHandTotal, PChandTotal):
    if sum(PChandTotal) <= 21 and sum(PChandTotal)< sum(userHandTotal):
        return True
    if sum(userHandTotal) <= 10:
        return True
    return False
    
def BlackJack():
    userHand = selectCards()
    PCHand = selectCards()
    print(f"{userName}'s hand: {userHand}")
    print(f"PC hand: {PCHand}")
    
    while sum(userHand) < 21:
        moreCard = input("Do you want card?: ").lower()
        if moreCard == "yes":    
            userHand.append(random.choice(cards))
            elevenToOne(userHand)
            print(userHand)
            print(PCHand[1])
            
        else:
            break
    while PC_cardDecision(userHand,PCHand):
        PCHand.append(random.choice(cards))
        elevenToOne(PCHand)
            
    print(f"{userName}'s hand: {userHand}")
    print(f"PC hand: {PCHand}")
        
    result = isBlackJack(userHand, PCHand)
    if result is True:
        print(result)
    elif sum(userHand) > 21:
        print(f"{userName} busted, PC won!")
    elif sum(PCHand) > 21:
        print(f"PC busted, Safak Won!")
    elif sum(userHand) > sum(PCHand):
        print(f"{userName} Won!")
    elif sum(PCHand) > sum(userHand):
        print(f"PC Won!")
    elif sum(PCHand) == sum(userHand):
        print(f"Draw, it is a tie.")
    else:
        print("PC won!")
    
BlackJack()
