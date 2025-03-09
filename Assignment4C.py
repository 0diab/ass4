from A4C_Functions import DisplayMainMenu, Deposit, Withdraw, CheckBalance

print("Welcome to the ATM!")
name = input("Please enter your name: ")
balance = float(input(("Enter your initial balance: $")))

q =1
while q:
    choice = DisplayMainMenu()

    match choice:
        case 1:
            balance = Deposit(balance)
        case 2:
            balance = Withdraw(balance)
        case 3:
            balance = CheckBalance(balance)
        case 4:
            print(f"Goodbye, {name}! Thank you for using the ATM.")
            break
        case _:
            print("Invalid choice. Please try again.")
    print()