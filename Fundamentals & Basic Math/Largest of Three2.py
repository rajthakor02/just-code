def find_largest(list):
    largest = list[0]
    for larg in list:
        if larg >= largest:
            largest = larg
    return largest

def how_many_numbers(list):
    n = int(input("Tell me how many numbers do you want to add: "))
    for i in range(1, n+1):
        list.append(int(input(f"Enter the number {i}: ")))
    largest = find_largest(list)
    print(f"The largest number is {largest}")


def main():
    print("This is the largest number finding program.")
    list = []
    while True:
        how_many_numbers(list)
        another = input("Do you want to exit or continue? (yes if want to continue otherwise tell no): ").strip().lower()
        if another != "yes":
            print("Goodbye, Have a nice day...")
            break

main()
