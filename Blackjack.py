import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_initial_hand():
    return [random.choice(cards), random.choice(cards)]

def adjust_ace_value(hand):
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

def blackjack_winner(player_hand, pc_hand, user):
    if sum(player_hand) == 21:
        return f"{user}, BlackJack, you won."
    if sum(pc_hand) == 21:
        return "PC, BlackJack, PC won."
    return None

def pc_decide_to_draw(pc_hand, user_hand):
    if sum(pc_hand) < 17:
        return True
    if sum(user_hand) <= 21 and sum(pc_hand) < sum(user_hand):
        return True
    return False

def play_blackjack(user):
    player_hand = get_initial_hand()
    pc_hand = get_initial_hand()

    print(f"{user}'s initial hand: {player_hand}")
    print(f"PC's initial hand: {pc_hand[1]}")

    while sum(player_hand) < 21:
        while True:
            more_card = input(f"Do you want a card, {user}? (yes/no): ").lower()
            if more_card in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if more_card == "yes":
            player_hand.append(random.choice(cards))
            adjust_ace_value(player_hand)
            print(f"{user}'s hand: {player_hand}")
        else:
            break

    while pc_decide_to_draw(pc_hand, player_hand):
        pc_hand.append(random.choice(cards))
        adjust_ace_value(pc_hand)

    print(f"{user}'s final hand: {player_hand}")
    print(f"PC's final hand: {pc_hand}")

    result = blackjack_winner(player_hand, pc_hand, user)
    if result:
        print(result)
    elif sum(player_hand) > 21:
        print(f"{user} busted, you lost!")
    elif sum(pc_hand) > 21:
        print("PC busted, you won!")
    elif sum(player_hand) > sum(pc_hand):
        print(f"{user}, you won!")
    elif sum(player_hand) == sum(pc_hand):
        print("Draw, it's a tie.")
    else:
        print("PC won!")

user = input("Welcome to blackJack, Enter your name: ")
playGame = input("Do you want to play blackjack? (yes/no): ").lower()
while playGame == "yes":
    clear()
    play_blackjack(user)
    playGame = input("Do you want to play again? (yes/no): ").lower()
