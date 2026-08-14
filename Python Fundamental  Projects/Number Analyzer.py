def cal_sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

def cal_avg(nums):
    total = cal_sum(nums)
    return total / len(nums)

def largest_num(nums):
    largest_num = nums[0]
    for num in nums:
        if num >= largest_num:
            largest_num = num
    return largest_num

def smallest_num(nums):
    smallest_num = nums[0]
    for i in nums:
        if i <= smallest_num:
            smallest_num = i
    return smallest_num

def even_odd(nums):
    even = 0 
    odd = 0 
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
def main():
    while True:
        try:
            n = int(input("Enter how many numbers you want to add: "))
        except ValueError:
            print("Please enter a valid integer for the count.")
            continue
        if n <= 0:
            print("Please enter a positive number greater than zero.")
            continue
        break

    nums = []
    for i in range(n):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue
            nums.append(num)
            break

    menu = (
        "What do you want to do?\n"
        "1) Sum\n"
        "2) Largest\n"
        "3) Smallest\n"
        "4) Even count\n"
        "5) Odd count\n"
        "6) Average\n"
        "7) Exit\n"
    )
    print(menu)
    what_next(nums)

def what_next(nums):
    while True:
        try:
            work = int(input("Select option number: "))
        except ValueError:
            print("Please enter a valid option number.")
            continue

        if work == 7:
            print("Goodbye.")
            break

        result(work, nums)

        another = input("Want to analyze more? (yes or no) ").strip().lower()
        if another != "yes":
            break
    

def result(work, nums):
    if work == 1:
        print(f"Total of the given numbers is {cal_sum(nums)}")
    elif work == 2:
        print(f"The largest given number is {largest_num(nums)}")
    elif work == 3:
        print(f"The smallest given number is {smallest_num(nums)}")
    elif work == 4:
        even_count, odd_count = even_odd(nums)
        print(f"Even count: {even_count}")
    elif work == 5:
        even_count, odd_count = even_odd(nums)
        print(f"Odd count: {odd_count}")
    elif work == 6:
        print(f"Average of given numbers is : {cal_avg(nums)}")
    elif work == 7:
        return
    else:
        print("Enter number according to the arrangement!\n")

main()