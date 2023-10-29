class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # method for deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} RS \nNew balance: {self.balance} RS")
        else:
            print("Invalid deposit amount.")

    # method for withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} RS \nNew balance: {self.balance} RS")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # method for calculate interest 
    def calculate_interest(self):
        pass 
    
    # method for deduct transaction fee
    def deduct_transaction_fee(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest calculated: {interest} RS")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, transaction_fee):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} RS")

    def deduct_transaction_fee(self):
        if self.balance >= self.transaction_fee:
            self.balance -= self.transaction_fee
            print(f"Transaction fee deducted: {self.transaction_fee} RS")
        else:
            print("Insufficient funds for transaction fee")
        print(f"Remaining balance: {self.balance}")



class BankCustomer:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    # method for create saving account
    def create_savings_account(self, account_number, initial_balance, interest_rate):
        savings_account = SavingsAccount(account_number, initial_balance, interest_rate)
        self.accounts[account_number] = savings_account
        print(f"Savings account {account_number} created for {self.name}.")
        print()

    # method for create checking account
    def create_checking_account(self, account_number, initial_balance, transaction_fee):
        checking_account = CheckingAccount(account_number, initial_balance, transaction_fee)
        self.accounts[account_number] = checking_account
        print(f"Checking account {account_number} created for {self.name}.")
        print()

    # method for check account balance
    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        else:
            return "Account not found."
    
    # method for get account details 
    def get_all_account_details(self):
        print(f"Account details for {self.name}:")
        for account_number, account in self.accounts.items():
            if isinstance(account, SavingsAccount):
                account_type = "Savings Account"
            elif isinstance(account, CheckingAccount):
                account_type = "Checking Account"
            else:
                account_type = "Unknown Account Type"

            print(f"Account Number: {account_number}")
            print(f"Account Type: {account_type}")
            print(f"Account Balance: {account.balance} RS")
            print()


# create saving account for customer 1
customer = BankCustomer("Abdul Rehman")

customer.create_savings_account("AR12345", 1000, 0.05)

print(f"{customer.name} Savings Account Balance: {customer.get_account_balance('AR12345')} RS")

print()

# create checking account for customer 1

customer.create_checking_account("AR54321", 1500, 10)
print(f"{customer.name} Checking Account Balance: {customer.get_account_balance('AR54321')} RS")
print()

# deposit and calculate interest

customer.accounts['AR12345'].deposit(500)
customer.accounts['AR12345'].calculate_interest()

print()

# withdraw an amount

customer.accounts['AR54321'].withdraw(100)
customer.accounts['AR54321'].deduct_transaction_fee()


print()
customer.get_all_account_details()

# create account account for customer 2

# customer1 = BankCustomer("Muhammad Sufyan")

# customer1.create_savings_account("MS12345", 2000, 0.05)



# print(f"{customer1.name} Savings Account Balance: {customer1.get_account_balance('MS12345')} RS")

# print()

# customer1.create_checking_account("MS54321", 1100, 10)
# print(f"{customer1.name} Checking Account Balance: {customer1.get_account_balance('MS54321')} RS")
# print()

# customer1.accounts['MS12345'].deposit(500)
# customer1.accounts['MS12345'].calculate_interest()

# print()

# customer1.accounts['MS54321'].withdraw(100)
# customer1.accounts['MS54321'].deduct_transaction_fee()


# print()
# customer1.get_all_account_details()
