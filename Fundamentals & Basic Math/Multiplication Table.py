def table(start, end):
    for i in range(start, end):
        print("\nTable of {i}")
        for j in range(1,11):
            print(f"{i} X {j} = {j*i}")
        pass

def main():
    while True:
        try:
            start = int(input("Enter the start table number: "))
        except ValueError:
            print("Enter correct integer!")
            continue

        try:
            end = int(input("Enter the end table number: "))
        except ValueError:
            print("Enter correct integer!")
            continue

        table(start, end)
        another = input("Do you want do it again? (yes or no) : ").strip().lower()
        if another != "yes":
            print("jay shree krishna...")
            break
main()

