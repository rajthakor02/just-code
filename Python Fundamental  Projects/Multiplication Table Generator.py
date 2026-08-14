def singletable(n):
    print(f"Table of {n} ")
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

def single_table():
    while True:
        try:
            n = int(input("Enter the number: "))
        except ValueError:
            print("Please enter a valid integer for the count.")
            continue
        if n <= 0:
            print("Please enter a positive number greater than zero.")
            continue
        break
    singletable(n)

def table_1to10():
    for n in range(1,11):
        print(f"\nTable of {n}")
        for i in range(1,11):
            print(f"{n} X {i} = {n*i}")

def custom_range(x,y):
    for n in range(x,y+1):
        print(f"\nTable of {n}")
        for i in range(1,11):
            print(f"{n} X {i} = {n*i}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def menu_loop():
    while True:
        choice = get_int("Select option number: ")

        if choice == 1:
            single_table()
        elif choice == 2:
            table_1to10()
        elif choice == 3:
            while True:
                start = get_int("Enter start of range: ")
                end = get_int("Enter end of range: ")
                if start <= 0 or end <= 0:
                    print("Please enter positive integers.")
                    continue
                if start > end:
                    print("Start should be less than or equal to end.")
                    continue
                break
            custom_range(start, end)
        elif choice == 4:
            print("Goodbye.")
            break
        else:
            print("Please select a valid option (1-4).")

def main():
    menu_text = (
        "What do you want to do?\n"
        "1. Print one table for a number\n"
        "2. Print tables 1 to 10\n"
        "3. Print custom range of tables\n"
        "4. Exit\n"
    )
    print(menu_text)
    menu_loop()


if __name__ == "__main__":
    main()

