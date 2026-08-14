def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            print("Not prime.")
            break
    else:
        print("Prime")

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