def add_nums(n, numbers):
    for i in range(n):
        numbers.append(int(input(f"Enter the number {i+1} : " )))

    total = 0
    for number in numbers:
        total += number

    print(total)
        
         

def main():
    numbers = []
    while True:
        try:
            n = int(input("Enter how many numbers sum you want: "))
        except ValueError:
            print("Enter possitive integer only!")
            continue

        add_nums(n, numbers)

        another = input("Do you want to do it again? (yes or no) :").strip().lower()
        if another != "yes":
            print("Bye bye...")
            break

main()