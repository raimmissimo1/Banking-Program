def show_balance(balance):
    print(f"Your balance is: {balance:.2f}₸")

def deposit():
    amount = float(input("Enter amount to deposit: "))

    if amount < 0:
        print("This is not a valid amount.")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("There is no such balance.")
        return 0
    elif amount < 0:
        print("This is not a valid amount.")
        return 0

    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice")

    print("Thank You,Have a nice day!")

if __name__ == "__main__":
    main()