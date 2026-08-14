def palindrome(n):
    if n == 0:
        return 0

    digits = []
    n = abs(n)

    while n > 0:
        digits.append(n % 10)
        n //= 10

    return digits, digits[::-1]

def palindrome2(n):
    digits, digits[::-1] = palindrome(n)
    if digits == digits[::-1]:
        print("palindrome")
    else :
        print("not")

def main():
    while True:
        try:
            n = int(input("Enter the number: "))
        except ValueError:
            print("Enter number again!")
            continue
        palindrome2(n)
        if input("You want to continue? (yes or no): ").strip().lower() != "yes":
            break  

main()