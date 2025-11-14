import random
import art
import os

cards = [11, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_card():
    for n in range (2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

def compare_hands():
    global game_end
    user = sum(user_cards)
    comp = sum(computer_cards)
    
    if is_blackjack(computer_cards):
        show_real_hand()
        print("You loose.")
        game_end = True

    elif user > comp:
        show_real_hand()
        print("You win")
        game_end = True
    elif user < comp:
        show_real_hand()
        print("You loose")
        game_end = True
    else:
        show_real_hand()
        print("Draw")
        game_end = True
    

def comp_plays():
    global game_end
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        if is_bust(computer_cards):
            show_real_hand()
            print("You win")
            game_end = True
            break
    if not game_end:
        compare_hands()



def get_another_card():
    global game_end
    hit = input("Do you want to draw another card (Y/n): ").lower().strip()
    if hit == 'y':
        user_cards.append(random.choice(cards))
        if is_bust(user_cards):
            show_real_hand()
            print("You loose.")
            game_end = True
    else:
        comp_plays()

def show_current_hand():
    print(F"Your hand: {user_cards} ({sum(user_cards)})")
    print(f"Computer's hand: [{computer_cards[0]}, ?]")

def show_real_hand():
    print(F"Your hand: {user_cards} ({sum(user_cards)})")
    print(f"Computer's hand: {computer_cards} ({sum(computer_cards)})")

def is_blackjack(check_cards):
    if sum(check_cards) == 21:
        return True
    else:
        return False
    

def is_bust(check_cards):
    if sum(check_cards) > 21:
        if 11 in check_cards:
            index = check_cards.index(11)
            check_cards[index] = 1
            if sum(check_cards) > 21:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(os.name)
os.system("clear") if os.name == "posix" else os.system("cls")

logo = art.logo
print(logo)

deal_card()
game_end = False

while not game_end:
    show_current_hand()

    if is_blackjack(user_cards):
        show_real_hand()
        print("Blackjack!, You win.")
        game_end = True
    
    else:
        get_another_card()
