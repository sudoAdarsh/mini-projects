import random
import art
import os

# Set of cards along with their values
cards = [11, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10, 10, 10, 10]

# Initial hands
user_cards = []
computer_cards = []

# Deal cards
def deal_card():
    for n in range (2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

# Compare hands
def compare_hands():
    global game_end
    user = sum(user_cards)
    comp = sum(computer_cards)
    
    # If computers gets BlackJack
    if is_blackjack(computer_cards):
        show_real_hand()
        print("You loose.")
        game_end = True

    # If player's hand is better than comp
    elif user > comp:
        show_real_hand()
        print("You win")
        game_end = True

    # If comp's hand is better than player's
    elif user < comp:
        show_real_hand()
        print("You loose")
        game_end = True
    
    # If both are equal 
    else:
        show_real_hand()
        print("Draw")
        game_end = True
    

def comp_plays():
    global game_end

    # Computer draws card until it's value is more than 17
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        # If value exceeded 17 computer looses
        if is_bust(computer_cards):
            show_real_hand()
            print("You win")
            game_end = True
            break
    if not game_end:
        compare_hands()

# Ask player for another card
def get_another_card():
    global game_end
    hit = input("Do you want to draw another card (Y/n): ").lower().strip()
    if hit == 'y':
        user_cards.append(random.choice(cards))
        # After getting card player's gets above 21 then it's their loss
        if is_bust(user_cards):
            show_real_hand()
            print("You loose.")
            game_end = True
    else:
        comp_plays()

# Show current hand of player and one card comp
def show_current_hand():
    print(F"Your hand: {user_cards} ({sum(user_cards)})")
    print(f"Computer's hand: [{computer_cards[0]}, ?]")

# Show real hand of comp
def show_real_hand():
    print(F"Your hand: {user_cards} ({sum(user_cards)})")
    print(f"Computer's hand: {computer_cards} ({sum(computer_cards)})")

# Check if sum is exactly 21 which results in win by BlackJack
def is_blackjack(check_cards):
    if sum(check_cards) == 21:
        return True
    else:
        return False
    

# Check if sum is more than 21 
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

# Clear previous game's screen
os.system("clear") if os.name == "posix" else os.system("cls")


# Print logo
logo = art.logo
print(logo)

# Deal initial hands
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
