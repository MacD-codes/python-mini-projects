def show_bal(balance):
    print(f"Your balance is Rs {balance}")


def deposit():
    amount = int(input("Enter the amount to deposit: Rs. "))
    if amount < 0:
        print("That is not valid")
        return 0
    else:
        print(f"Rs. {amount} deposited")
        return amount 


def withdraw(balance):
    amount = int(input("Enter the amount to be withdrawn: Rs. "))
    if amount > balance:
        print("Cannot withdraw! Insufficient Balance!!")
        return 0
    elif amount < 0:
        print("This is not valid")
        return 0
    else:
        print(f"Rs. {amount} withdrawn")
        return amount


def main():
    balance = 10000
    is_running = True

    while is_running:
        print("----------------- Banking Program ---------------")
        print("1. Show Balance")
        print("2. Add Deposit")
        print("3. Withdraw")
        print("4. Exit")

        user = input("Enter your choice (1-4): ")
        if user == "1":
            show_bal(balance)
        elif user == "2":
            balance += deposit()
        elif user == "3":
            balance -= withdraw(balance)
        elif user == "4":
            is_running = False
        else:
            print("Not valid choice :(")
    print("Have a nice day :)")


if __name__ == "__main__":
    main()
