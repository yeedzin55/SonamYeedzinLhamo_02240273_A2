class PokemonBinder:
    def __init__(self):
        # Dictionary to store cards with Pokedex number as key and value as (page, row, column)
        self.cards = {}
        self.max_pokedex = 1025
        self.cards_per_page = 64
        self.grid_size = 8  # 8x8 grid per page

    def calculate_position(self, pokedex_number):
        ("""Algorithm: Calculates the card's page number and (row, column) position in the binder.
        - Each page has 64 slots (8x8)
        - Cards are placed left-to-right, top-to-bottom""")
        index = pokedex_number - 1
        page = index // self.cards_per_page + 1
        position = index % self.cards_per_page
        row = position // self.grid_size + 1
        col = position % self.grid_size + 1
        return page, row, col

    def add_card(self, pokedex_number):
        ("""Adds a card to the binder if valid and not a duplicate.
        Returns status message with card location or error.""")
        if not (1 <= pokedex_number <= self.max_pokedex):
            return "Error: Invalid Pokedex number."
        if pokedex_number in self.cards:
            return f"Pokedex #{pokedex_number} already exists in binder."

        page, row, col = self.calculate_position(pokedex_number)
        self.cards[pokedex_number] = (page, row, col)
        return f"Page: {page}\nPosition: Row {row}, Column {col}\nStatus: Added Pokedex #{pokedex_number} to binder"

    def reset_binder(self):
        ("""Clears the binder contents.
        Data is deleted by clearing the dictionary.""")
        self.cards.clear()

    def view_binder(self):
        ("""Returns the contents of the binder with positions and completion stats.""")
        if not self.cards:
            return "The binder is empty.\nTotal cards in binder: 0\nCompletion: 0%"

        output = ["Current Binder Contents:"]
        for pokedex_number in sorted(self.cards):
            page, row, col = self.cards[pokedex_number]
            output.append(f"Pokedex #{pokedex_number}: Page {page} Position: Row {row}, Column {col}")

        total_cards = len(self.cards)
        percent = round((total_cards / self.max_pokedex) * 100, 1)
        if total_cards == self.max_pokedex:
            output.append("You have caught them all!!")
        output.append(f"Total cards in binder: {total_cards}\nCompletion: {percent}%")
        return "\n".join(output)

# Command-line interface for interacting with the binder
class PokemonBinderManager:
    def __init__(self):
        self.binder = PokemonBinder()

    def run(self):
        print("Welcome to Pokemon Card Binder Manager!")
        while True:
            print("""Main Menu:
              1. Add Pokemon card
              2. Reset binder
              3. View current placements
              4. Exit""")
            choice = input("Select option: ").strip()
            if choice == '1':
                try:
                    number = int(input("Enter Pokedex number: ").strip())
                    print(self.binder.add_card(number))
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == '2':
                confirm = input("WARNING: This will delete ALL Pokemon cards from the binder. " \
                  "This action cannot be undone. Type CONFIRM to reset or 'EXIT' to return to the Main Menu: ").strip().upper()
                if confirm == 'CONFIRM':
                    self.binder.reset_binder()
                    print("The binder reset was successful! All cards have been removed.")
                else:
                    print("Reset cancelled. Returning to main menu.")
            elif choice == '3':
                print(self.binder.view_binder())
            elif choice == '4':
                print("Thank you for using Pokemon Card Binder Manager!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    manager = PokemonBinderManager()
    manager.run()