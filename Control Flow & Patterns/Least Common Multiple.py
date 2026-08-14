def a_greater_b():
    while True:
        try:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
        except ValueError:
            print("Enter possitive integer!")
            continue

        if a > b:
            return a, b
        else:
            print(f"{a} is not greater then {b}. a>b")

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcd(a, b, c):
    get_lcd = abs(a * b) / c
    return get_lcd

def main():
    a, b = a_greater_b()
    result_gcd = gcd(a, b)
    result_lcd = lcd(a, b, result_gcd)
    print(f"The GCD({a},{b}) : {result_gcd}")
    print(f"The LCD({a},{b}) : {result_lcd}")
    
main()