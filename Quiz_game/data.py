import requests

class Opentb:

    def __init__(self): 
        self.response = requests.get(f"https://opentdb.com/api.php?amount=10&difficulty={self.difficulty()}&type=boolean")

        self.data = self.response.json()


            
    def difficulty(self):
        """Unfortunately Open trivia db dont have much of question for hard difficulty in most if not all categories so intead of making it we get all the question we can get i got lazy and changed all the difficulty to return 'any' which means give what ever it has.
        if you feel cheated then fix it idgaf anymore it's 3:49 am
        
        Update : Fuck this man you cannot call api more than once in 5 seconds so you can't handle the index error so you need to freeze the program for 5 sec using os module i dont have patience to set that up so i am removng categories in total this should make all the difficulties work in general"""
        foo = input("Set Difficulty to ('Easy', 'Medium', 'Hard'): ").lower().strip()

        if foo.startswith('e'):
            print("Difficulty is set to Easy.")
            return 'easy'
        if foo.startswith('m'):
            print("Difficulty is set to medium.")
            return 'medium'
        if foo.startswith('h'):
            print("Difficulty is set to Hard.")
            return 'hard'
        else:
            print("Choose a valid Difficulty!")
            return self.difficulty()
