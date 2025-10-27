import random
import art

logo = print(art.logo)


def range_of_game():
    print("format: \"from, to\" (eg: Range: 1, 100)")
    try:
        r1, r2 = input("\nRange of numbers: ").split(',')
        r1 = int(r1)
        r2 = int(r2)
        print(f"Guess my number between {r1} and {r2}")
        return r1,r2
    except:
        print("Enter the range in correct format!")
        return range_of_game()


def mode():
    foo = input("\nSelect game mode 'Easy' or 'Hard': ").lower().strip()
    try:
        if foo.startswith('e'):
            print("\nYou have selected Easy mode, You have 10 chances to guess the number.")
            return 10
        elif foo.startswith('h'):
            print("\nYou have selected Hard mode, You have 5 chances to guess the number.")
            return 5
        else:
            print("Choose correct difficulty!")
            return mode()
    except:
        print("Invalid input, ",  end='')
        return mode()


def main():
    print("== == == WELCOME == == ==")
    chances = mode()

    print("Great, lets choose range of numbers for number to be guessed from")
    num_1 , num_2 = range_of_game()
    number = random.randint(num_1, num_2)

    attempts = 0
    game_over = False

    while not game_over:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Enter a valid input!")
            guess = int(input("\nEnter your guess: "))

        if guess < number:
            print(f"My number is greater than {guess}")
            chances -= 1
            attempts += 1
            print(f"{chances} chances left, Guess again")
        elif guess > number:
            print(f"My number is less than {guess}")
            chances -= 1
            attempts += 1
            print(f"{chances} chances left, Guess again")
        else:
            print(f"Well done! it took you {attempts} attempts to guess this number.")
            game_over = True

        if chances == 0:
            print("\nAhh, It looks like you have 0 chances left.")
            print(f"well my number was {number}")
            print("Thanks for playing.")
            game_over = True

if __name__ == "__main__":
    main()