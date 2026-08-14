def find_prime(n):
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

def is_prime(start, end):
    prime = [n for n in range(start, end+1) if find_prime(n)]
    print(prime)

def main():
    while True:
        try:
            start = int(input("Enter a start number: "))
            end = int(input("Enter a last number: "))
        except ValueError:
            print("Enter correct value!")
            continue
        is_prime(start, end)

        another = input("Do you want to continue? (yes or no): ").strip().lower()
        if another != "yes":
            break
main()