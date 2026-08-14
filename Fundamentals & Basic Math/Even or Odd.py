def even_or_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def main():
    while True:
        print ("When you want to exit just enter 0")
        try:
            n = int(input("Enter the number: "))
        except ValueError:
            print("Enter integer only.")
            continue

        if n == 0:
            print("Goodbye...")
            break

        even_or_odd(n)


main()