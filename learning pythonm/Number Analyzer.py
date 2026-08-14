def get_numbers(n):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return numbers

def cal_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def cal_average(numbers):
    total = cal_sum(numbers)
    return total / len(numbers)

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest 

def find_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num 
    return smallest 

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

def main():
    n = int(input("How many number do you want to enter? "))
    numbers = get_numbers(n)

    total = cal_sum(numbers)
    average = cal_average(numbers)
    largest = find_largest(numbers)
    smallest = find_smallest(numbers)
    even_count, odd_count = count_even_odd(numbers)

    print ("\n---Result---")
    print(f"Numbers entered: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Even count: {even_count}")
    print(f"odd count: {odd_count}")

main()