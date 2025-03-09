def DisplayMainMenu():
    print("ATM Main Menu: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Please choose an option (1-4): "))
    return choice

def Deposit(balance):
    deposit = float(input("Enter the amount to deposit: $ "))
    balance += deposit
    print(f"Deposited ${deposit}. New balance: ${balance}")
    return balance

def Withdraw(balance):
    withdraw = float(input("Enter the amount to Withdraw: $ "))
    balance -= withdraw
    print(f"Deposited ${withdraw}. New balance: ${balance}")
    return balance

def CheckBalance(balance):
    print(f"Your current balance is: {balance}")
    return balance

