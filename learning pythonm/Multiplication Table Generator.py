

def table1to10():
    for i in range(1,11):
        print(f"\nTable of {i}")
        get_table(i)

def printcustomrange():
    a = int(input("Enter the starting table:"))
    b = int(input("Enter the ending table:"))
    for i in range(a, b):
        print("\nTable of {i}")
        for j in range(1,11):
            print(f"{i} X {j} = {j*i}")
        pass
        

def get_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

def main():
    print("""       ===== MENU =====
    1. Print one table
    2. Print tables 1-10
    3. Print custom range
    4. Exit""")
    c = int(input(f"Choice what you want to do by their given number:"))
    choices(c)

def choices(choice):
    if choice == 1:
        n = int(input("Enter the number:"))
        print("")
        get_table(n)
    elif choice == 2:
        table1to10()
    elif choice == 3:
        printcustomrange()
    elif choice == 4:
        print("Bye bye")
    else:
        print("Uper wo number dikh raha hai kya tujhe?")
        breakpoint

main()
