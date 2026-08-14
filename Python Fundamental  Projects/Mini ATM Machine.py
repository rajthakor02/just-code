def get_float(prompt):
    while True:
        try:
            amount = float(input(prompt))
        except ValueError:
            print("Enter a valid number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return amount


def deposit(balance, history):
    amount = get_float("Enter how much amount you want to deposit: ")
    balance += amount
    history.append(f"Deposit: +{amount:.2f} | Balance: {balance:.2f}")
    print(f"Deposited: {amount:.2f}")
    return balance


def withdraw(balance, history):
    amount = get_float("Enter how much amount you want to withdraw: ")

    if amount > balance:
        print("Insufficient balance.")
        return balance

    balance -= amount
    history.append(f"Withdraw: -{amount:.2f} | Balance: {balance:.2f}")
    print(f"Withdrawn: {amount:.2f}")
    return balance


def show_balance(balance):
    print(f"Current balance: {balance:.2f}")


def show_history(history):
    print("Transaction history:")
    if not history:
        print("No transactions yet.")
        return

    for item in history:
        print(item)


def menu_selection():
    balance = 0.0
    history = []
    menu = (
        "1 Deposit\n"
        "2 Withdraw\n"
        "3 Check Balance\n"
        "4 Exit"
    )

    while True:
        print(menu)

        try:
            slt = int(input("Select the option: "))
        except ValueError:
            print("Enter valid option.")
            continue

        if slt == 1:
            balance = deposit(balance, history)
        elif slt == 2:
            balance = withdraw(balance, history)
        elif slt == 3:
            show_balance(balance)
            show_history(history)
        elif slt == 4:
            print("Goodbye.")
            break
        else:
            print("Enter valid option.")


def main():
    menu_selection()

main()