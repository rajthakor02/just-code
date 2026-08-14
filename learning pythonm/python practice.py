def get_numbers(n):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter the number {i+1} : "))
        numbers.append(num)
    return numbers 

def cal_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total 

def cal_average(numbers):
    average = cal_sum(numbers)/len(numbers)
    return average

def find_even_odd(numbers):
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd



def main():
    n = int(input("How many numbers you want to enter?"))
    numbers = get_numbers(n)
    sum = cal_sum(numbers)
    average = cal_average(numbers)
    even, odd = find_even_odd(numbers)
    print("sum:",sum)
    print(f"Average: {average}")
    print(f"Even:{even}")
    print(f"Odd:{odd}")
    print(f"")

main()