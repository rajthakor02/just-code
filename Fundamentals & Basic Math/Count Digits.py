def count(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count 

def main():
    while True:

        try:
            n = int(input("Enter the number : "))
        except ValueError:
            print("Enter the correct value!")
            continue

        count(n)
        print(count(n))
main()

        