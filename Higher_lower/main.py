import data
import art
import random
import os

logo = art.logo
vs = art.vs

def display(info):
    return f"{info["name"]}, a {info["description"]}, from {info["country"]}."

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


choice_a = random.choice(data.data)
choice_b = random.choice(data.data)

def check(a, b):
    v1 = a["follower_count"]
    v2 = b["follower_count"]

    if v1 > v2:
        return a
    else:
        return b

def choose():
    ask = input("Choose: ").lower().strip()
    return choice_a if ask.startswith('a') else choice_b
    

def main():
    global choice_a, choice_b
    gameover = False
    score = 0
    while not gameover:
        print(logo)
        print("Compare A:", display(choice_a))
        print(vs)
        print("Against B:", display(choice_b))
        choice = choose()
        if choice == check(choice_a, choice_b):
            print("You win")
            score += 1
            clear()
            choice_a = choice
            choice_b = random.choice(data.data)
        else:
            print("You loose")
            print(f"Your total score is {score}.")
            gameover = True
main()