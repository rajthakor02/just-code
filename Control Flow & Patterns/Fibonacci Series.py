def fibonacci(n):
    list = []
    a, b = 0, 1
    for _ in range(n):
        list.append(a)
        a, b = b, b+a
    print(list)


def main():
    try:
        term = int(input("Enter the number of terms: "))
    except ValueError:
        print("Enter a positive whole number.")
        return

    if term <= 0:
        print("Enter a positive whole number.")
        return

    fibonacci(term)


main()