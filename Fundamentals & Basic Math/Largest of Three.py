def Largest_of_Three(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is the largest")
    elif b >= a and b >= c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")
def input_f():
    while True:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        c = int(input("Enter the third number:"))
        Largest_of_Three(a, b, c)
        break

def main():
    print("This is the largest number finding program.")
    while True:
        input_f()
        another = input("Do you want to exit or continue? (yes if want to continue otherwise tell no): ").strip().lower()
        if another != "yes":
            print("Goodbye, Have a nice day...")
            break

main()