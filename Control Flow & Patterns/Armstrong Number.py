def is_armstrong(n):
    num_digits = 0
    temp = n
    while temp > 0:
        num_digits += 1
        temp //= 10 #if the temp number is 153 then this quiation give result 15

    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit**num_digits
        temp //= 10

    return total == n

def main1():
    while True:
        try:
            n = int(input("Enter the number: "))
        except ValueError:
            print("Enter a possitive integer!")
            continue

        if is_armstrong(n):
            print(f"The number {n} is armstrong number.")
        else:
            print(f"The number {n} is not armstrong number.") 
        main()   

def total(start, end):
    armstrong = [n for n in range(start, end+1) if is_armstrong(n)]
    print(armstrong)

def custome_range():
    while True:
        try:
            start = int(input("Enter a start number: "))
            end = int(input("Enter a last number: "))
        except ValueError:
            print("Enter correct value!")
            continue
        total(start, end)
        main()

def main():
    menu = (
        "\n1. Know about just one number.\n"
        "2. Want to find armstrong in custome range.\n"
        "3. For exit."
    )
    print(menu)
    while True:
        try:
            n = int(input("Select the option number: "))
        except ValueError:
            print("just select one number between 1 and 2!")
            continue

        if n == 1:
            main1()
        elif n == 2:
            custome_range()
        elif n == 3:
            break
main()
