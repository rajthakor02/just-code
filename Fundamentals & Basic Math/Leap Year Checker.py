def leap(year):
    if year % 4 ==0:
        print("It is leap year.")
    elif year % 100 == 0:
        print("It is not a leap year but it is a century year.")
    elif year % 400 == 0:
        print("It is leap year.")
    else:
        print("Is is not leap year.")

def main():
    while True:
        try:
            year = int(input("Enter the year you wanna know it is leap or not: "))
        except ValueError:
            print("Enter correct integer!")
            continue

        leap(year)
        another = input("Do you want to know about other yeaer? (yes or no) :").strip().lower()
        if another != "yes":
            print("Bye bye...")
            break
main()