class PokemonBinder:
    def __init__(self):
        self.cards = {}  # Dictionary to store cards with Pokedex number as key
        self.max_pokedex = 1025
        self.cards_per_page = 64
        self.grid_size = 8  # 8x8 grid per page
    def calculate_position(self, pokedex_number):
        index = pokedex_number - 1
        page = index // self.cards_per_page + 1
        row = (index % self.cards_per_page) // self.grid_size + 1
        col = (index % self.cards_per_page) % self.grid_size + 1
        return page, row, col

    def add_card(self, pokedex_number):
        if not (1 <= pokedex_number <= self.max_pokedex):
            return "Error: Invalid Pokedex number."
        if pokedex_number in self.cards:
            return f"Pokedex #{pokedex_number} already exists in binder."

        page, row, col = self.calculate_position(pokedex_number)
        self.cards[pokedex_number] = (page, row, col)
        return f"Added Pokedex #{pokedex_number} to Page {page}, Row {row}, Column {col}."

    def reset_binder(self):
        self.cards.clear()
        return "Binder has been reset."

    def view_binder(self):
        if not self.cards:
            return "The binder is empty."

        output = ["Binder Contents:"]
        for pokedex_number in sorted(self.cards):
            page, row, col = self.cards[pokedex_number]
            output.append(f"Pokedex #{pokedex_number}: Page {page}, Row {row}, Column {col}")

        total_cards = len(self.cards)
        completion = (total_cards / self.max_pokedex) * 100
        output.append(f"Total cards: {total_cards}, Completion: {completion:.1f}%")
        return "\n".join(output)


class PokemonBinderManager:
    def __init__(self):
        self.binder = PokemonBinder()

    def run(self):
        print("Welcome to Pokemon Binder Manager!")
        while True:
            print("\nMenu:")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View binder")
            print("4. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                try:
                    pokedex_number = int(input("Enter Pokedex number: ").strip())
                    print(self.binder.add_card(pokedex_number))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == '2':
                confirm = input("Type 'CONFIRM' to reset the binder or anything else to cancel: ").strip().upper()
                if confirm == 'CONFIRM':
                    print(self.binder.reset_binder())
                else:
                    print("Reset cancelled.")
            elif choice == '3':
                print(self.binder.view_binder())
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = PokemonBinderManager()
    manager.run()
