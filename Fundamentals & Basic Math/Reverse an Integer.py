def reverse_int(n):
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    print(rev)

def main():
    while True:
        try:
            n = int(input("Enter number: "))
        except ValueError:
            print("Enter correct value!")
            continue

        reverse_int(n)
        break

main()