import random

class MiniGames:
    def __init__(self):
        self.total_score = 0
        self.pokemon_binder = []

    def display_menu(self):
        print("""Select a function (0-5):
          1. Guess Number Game
          2. Rock Paper Scissors Game
          3. Trivia Pursuit Game
          4. Pokemon Card Binder Manager
          5. Check Current Overall Score
          0. Exit Program""")

#Guess number game 
    def guess_number_game(self):
        print("\nWelcome to Guess the Number!")
        number = random.randint(1, 10)
        attempts = 0
        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
                attempts += 1
                if guess == number:
                    print("Correct!")
                    self.total_score += max(0, 10 - attempts)
                    break
                else:
                    print("Incorrect, try again.")
            except ValueError:
                print("Please enter a valid number.")

# rock paper scissors game
    def rock_paper_scissors(self):
        print("\nWelcome to Rock Paper Scissors!")
        options = ['rock', 'paper', 'scissors']
        wins = 0
        for _ in range(3):
            user = input("Choose rock, paper or scissors: ").lower()
            if user not in options:
                print("Invalid choice.")
                continue
            computer = random.choice(options)
            print(f"Computer chose {computer}")
            if user == computer:
                print("It's a tie!")
            elif (user == 'rock' and computer == 'scissors') or \
                 (user == 'paper' and computer == 'rock') or \
                 (user == 'scissors' and computer == 'paper'):
                print("You win!")
                wins += 1
            else:
                print("You lose!")
        self.total_score += wins

# Trivia pursuit quiz game
    def trivia_pursuit(self):
        print("\nWelcome to Trivia Pursuit!")
        questions = {
            "Science": ("What planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Earth"], 0),
            "History": ("Who was the first president of the USA?", ["Lincoln", "Washington", "Jefferson", "Adams"], 1),
        }
        correct = 0
        for category, (q, options, ans_index) in questions.items():
            print(f"\nCategory: {category}\n{q}")
            for i, opt in enumerate(options):
                print(f"{i + 1}. {opt}")
            try:
                choice = int(input("Enter your answer (1-4): ")) - 1
                if choice == ans_index:
                    print("Correct!")
                    correct += 1
                else:
                    print("Incorrect.")
            except ValueError:
                print("Invalid input.")
        self.total_score += correct

    def pokemon_binder_manager(self):
        while True:
            print("""Pokemon Binder Menu:
              1. Add Pokemon Card
              2. Reset Binder
              3. View Binder
              4. Exit to Main Menu""")
            choice = input("Choose an option: ")
            if choice == '1':
                name = input("Enter Pokemon name: ")
                self.pokemon_binder.append(name)
                print(f"{name} added to binder.")
            elif choice == '2':
                self.pokemon_binder.clear()
                print("Binder reset.")
            elif choice == '3':
                print("\nCurrent Binder:")
                for i, card in enumerate(self.pokemon_binder):
                    print(f"{i + 1}. {card}")
                if not self.pokemon_binder:
                    print("Binder is empty.")
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def show_score(self):
        print(f"\nTotal Score: {self.total_score}\n")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.guess_number_game()
            elif choice == '2':
                self.rock_paper_scissors()
            elif choice == '3':
                self.trivia_pursuit()
            elif choice == '4':
                self.pokemon_binder_manager()
            elif choice == '5':
                self.show_score()
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 0 to 5.")

if __name__ == "__main__":
    mini_games = MiniGames()
    mini_games.run()
