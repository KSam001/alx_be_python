class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to account_balance if amount is positive."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Deduct amount from account_balance if sufficient funds and amount is positive."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
