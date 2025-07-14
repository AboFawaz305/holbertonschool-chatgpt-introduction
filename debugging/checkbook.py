#!/usr/bin/python3


class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance.
    """

    def __init__(self):
        """
        Initializes the checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a positive amount to the balance.

        Parameters:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw an amount from the balance if sufficient funds exist.

        Parameters:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Display the current balance.
        """
        print(f"Current Balance: ${self.balance:.2f}")


def get_float_input(prompt):
    """
    Prompt the user repeatedly until a valid positive float is entered.

    Parameters:
        prompt (str): The prompt text to display.

    Returns:
        float: The validated positive float entered by the user.
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value < 0:
                print("Please enter a positive amount.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """
    Runs the interactive checkbook command-line interface.
    Supports deposit, withdraw, balance inquiry, and exit commands.
    """
    cb = Checkbook()
    while True:
        action = (
            input("What would you like to do? (deposit, withdraw, balance, exit): ")
            .strip()
            .lower()
        )

        if action == "exit":
            break
        elif action == "deposit":
            amount = get_float_input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == "withdraw":
            amount = get_float_input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == "balance":
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
