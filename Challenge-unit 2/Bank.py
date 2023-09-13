class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Amount must be greater than zero."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ₹{self.__account_balance}"

account = BankAccount("123456789", "Siva", 1000.0)


print(account.display_balance()) 
print(account.deposit(500))       
print(account.withdraw(1500)) 