import random

cards = [11, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_card():
    for n in range (2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

def comp_plays():
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))



def get_another_card():
    hit = input("Do you want to draw another card (Y/n): ").lower().strip()
    if hit == 'y':
        user_cards.append(random.choice(cards))
        is_blackjack()
    else:
        comp_plays()


def is_blackjack():
    user = sum(user_cards)
    comp = sum(computer_cards)

    if user == 21:
        print("You win")
    elif comp == 21:
        print("You loose")
    elif user > 21:
        if 11 in user_cards:
            index = user_cards.index(11)
            user_cards[index] = 1
            if user > 21:
                print("You loose")
            else:
                get_another_card()
        else:        
            print("You loose")
    else:
        get_another_card()
        if comp > 21:
            print("You loose")
        else:
            if user < comp:
                print("You loose")
            elif user > comp:
                print("You win")
            else:
                print("Draw")


deal_card()
is_blackjack()