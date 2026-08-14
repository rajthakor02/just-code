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

def main():
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

        if input("Do you want to continue? (yes or no) :").strip().lower() != "yes":
            break
main()