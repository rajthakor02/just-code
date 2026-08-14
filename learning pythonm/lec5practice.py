# wap to find the sum of first n numbers. using while
# n = int(input("enter the number : "))
# i = 0
# counter = 1
# while counter <= n:
#     i += counter
#     counter += 1

# print(f"the sum of the first {n} numbers:",i)

#n number factorial

n = int(input("enter the number : "))
factorial = 1
for i in range(1,n+1):
    factorial *= i
    i += 1
print(factorial)