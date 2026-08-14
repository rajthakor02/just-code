def is_prime(n):
    if n < 2:
        return False
    elif n in (2,3):
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        try:
            n = int(input("Enter a number: "))
        except ValueError:
            print("Enter correct value!")
            continue
        is_prime(n)

        another = input("Do you want to continue? (yes or no): ").strip().lower()
        if another != "yes":
            break
main()