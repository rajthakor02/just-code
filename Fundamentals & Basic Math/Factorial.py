def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    print(fact)

def main():
    while True:
        try:
            n = int(input("Enter the number which factorial you want: "))
        except ValueError:
            print("Enter possitive integer only!")
            continue

        factorial(n)

        another = input("Do you want to do it again? (yes or no) :").strip().lower()
        if another != "yes":
            print("Bye bye...")
            break

main()