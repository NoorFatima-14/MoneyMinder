class Transaction:
    def __init__(self, transaction_id, date, amount, category, description):
        self.transaction_id = transaction_id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return (f"ID: {self.transaction_id}, Date: {self.date}, "
                f"Amount: {self.amount}, Category: {self.category}, "
                f"Description: {self.description}")


class Finance_Manager:
    def __init__(self):
        self.transactions = []
        self.next_id = 1

    def add_transaction(self):
        num_transactions = int(input("How many transactions do you want to enter? "))
        for _ in range(num_transactions):
            date = input("Enter transaction date (DD/MM/YYYY): ")
            amount = float(input("Enter transaction amount: "))
            category = input("Enter Transaction Category (Income/Food/Transport/Utilities/Entertainment): ")
            description = input("Enter transaction description: ")

            transaction = Transaction(self.next_id, date, amount, category, description)
            self.transactions.append(transaction)
            self.next_id += 1
        print("*********************************")
        print("Transaction(s) added successfully!")
        print("*********************************")

    def view_transaction(self):
        print("\n1. View all Transactions")
        print("2. View Transactions filtered by date range")
        option = input("Please select the option: ")

        if option == '1':
            if not self.transactions:
                print("No transactions found.")
            else:
                for transaction in self.transactions:
                    print(transaction)
        elif option == '2':
            start_date = input("Enter start date (DD/MM/YYYY): ")
            end_date = input("Enter end date (DD/MM/YYYY): ")
            found = False
            for transaction in self.transactions:
                if start_date <= transaction.date <= end_date:
                    print(transaction)
                    found = True
            if not found:
                print("No transactions found in the given date range.")
        else:
            print("Invalid option selected. Please try again.")
        print("*********************************")


    def save_transactions(self):
        try:
            with open("transactions.txt", "w") as file:
                for transaction in self.transactions:
                    file.write(f"{transaction.transaction_id},{transaction.date},{transaction.amount},"
                               f"{transaction.category},{transaction.description}\n")
            print("Transactions saved successfully!")
        except Exception as e:
            print(f"An error occurred while saving transactions: {e}")
        print("*********************************")

    def load_transactions(self):
        try:
            with open("transactions.txt", "r") as file:
                for line in file:
                    transaction_id, date, amount, category, description = line.strip().split(',')
                    transaction = Transaction(int(transaction_id), date, float(amount), category, description)
                    self.transactions.append(transaction)
                    self.next_id = int(transaction_id) + 1
            print("Transactions loaded successfully!")
        except FileNotFoundError:
            print("No saved transactions found.")
        except Exception as e:
            print(f"An error occurred while loading transactions: {e}")
        print("*********************************")


def main():
    manager = Finance_Manager()
    print("++++++++++++ WELCOME TO MoneyMinder ++++++++++++")

    while True:
        print("\nMain Menu:")
        print("1. Add Transaction")
        print("2. View Transaction")
        print("3. Save Transactions")
        print("4. Load Transactions")
        print("5. Exit")

        choice = input("Please select an option (1-6): ")

        if choice == "1":
            manager.add_transaction()
        elif choice == "2":
            manager.view_transaction()

        elif choice == "3":
            manager.save_transactions()
        elif choice == "4":
            manager.load_transactions()
        elif choice == "5":
            print("*********************************")
            print("Exiting the program. Goodbye!")
            print("*********************************")
            break
        else:
            print("*********************************")
            print("Invalid option. Please select a valid option.")
            print("*********************************")


if __name__ == "__main__":
    main()
