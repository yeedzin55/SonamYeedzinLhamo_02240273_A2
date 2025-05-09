import random
import SonamYeedzinLhamo_02240273_A2_PB as PCB # (PCB = Pokemon Card Binder)

class MiniGames:
    def __init__(self):
        self.total_score = 0
        self.pokemon_binder = []

    def display_menu(self):
        print("\nSelect a function (0-5):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall Score")
        print("0. Exit Program")

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
                print("Incorrect, try again.")
            except ValueError:
                print("Please enter a valid number.")

    def rock_paper_scissors(self):
        print("\nWelcome to Rock Paper Scissors!")
        options = ['rock', 'paper', 'scissors']
        wins = 0
        for _ in range(3):
            user = input("Choose rock, paper, or scissors: ").lower()
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

    def trivia_pursuit(self):
        print("\nWelcome to Trivia Pursuit!")
        questions = [
            ("What planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Earth"], 0),
            ("Who was the first president of the USA?", ["Lincoln", "Washington", "Jefferson", "Adams"], 1)
        ]
        correct = 0
        for question, options, answer in questions:
            print(f"\n{question}")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            try:
                choice = int(input("Enter your answer (1-4): ")) - 1
                if choice == answer:
                    print("Correct!")
                    correct += 1
                else:
                    print("Incorrect.")
            except ValueError:
                print("Invalid input.")
        self.total_score += correct

    pokemon_binder_manager = PCB.PokemonBinderManager()
    def add_pokemon_card(self):
        pokedex_number = input("Enter Pokedex number: ")
        if pokedex_number.isdigit():
            self.pokemon_binder.append(pokedex_number)
            print(f"Added Pokedex #{pokedex_number} to binder.")
        else:
            print("Invalid Pokedex number.")
    def pokemon_binder_manager(self):
        print("\nWelcome to the Pokemon Binder Manager!")
        self.pokemon_binder = []    
        self.pokemon_binder_manager = PCB.PokemonBinderManager()
        self.pokemon_binder_manager.run()   
        while True:
            print("\nPokemon Binder Menu:")
            print("1. Add Pokemon Card")
            print("2. Reset Binder")
            print("3. View Binder")
            print("4. Exit to Main Menu")
            choice = input("Choose an option: ").strip()
            if choice == '1':
                name = input("Enter Pokemon name: ")
                self.pokemon_binder.append(name)
                print(f"{name} added to binder.")
            elif choice == '2':
                self.pokemon_binder.clear()
                print("Binder reset.")
            elif choice == '3':
                if self.pokemon_binder:
                    print("\nCurrent Binder:")
                    for i, card in enumerate(self.pokemon_binder, 1):
                        print(f"{i}. {card}")
                else:
                    print("Binder is empty.")
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def show_score(self):
        print(f"\nTotal Score: {self.total_score}")

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
    MiniGames().run()
