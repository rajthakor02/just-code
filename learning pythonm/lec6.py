# def sum(a, b):
#     s = a + b
#     return s
# print (sum(3, 5))
# print (sum(10, 20))
# print (sum(-1, 1))

# def sum(a, b):
#     s = a + b
#     print(s)
#     return s
# sum(3, 5)

# def print_hello():
#     print("Hello, World!")

#average of 3 numbers
# def average(a, b, c):
#     avg = (a + b + c) / 3
#     return avg
# i1 = int(input("Enter the first number:"))
# i2 = int(input("Enter the second number:"))
# i3 = int(input("Enter the third number:"))
# avg = average(i1,i2,i3)
# print (f"The average of given number is {avg}.")


#wap to print the lenght of a list 
# cities = ["mumbai", "vadodara", "noida"]
# heroes = ["spider man", "iron man", "saktiman", "thor", "capton america"]

# def printl(list):
#     for item in list:
#         print(item, end=" ")

# printl(cities)


#find feactorial
# m = int(input("enter the number : "))
# def cal(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print (fact)
#     return fact 
# cal(m)

# convert usd to inr
# usd = int(input("USD:"))
# rupee = 95.23

# def cal(a, b):
#     rupee = a * b
#     print(f"The {a} in indian rupee {rupee},")
#     return 
# cal(usd, rupee)

#2
# def converting(usd_val):
#     inr_val = usd_val * 95.23
#     print(usd_val, "usd =" , inr_val,"inr")

# converting(5)

# def oddeven():
#     n = int(input("Enter the number : "))
#     if n % 2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")

# oddeven()


#recursion function    
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show(10)

#return n!
# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(4))


# i = int(input("int:"))
# def sum(n):
#     if n == 0:
#         return 0
#     return sum(n-1) + n

# sumcal = sum(i)
# print(sumcal)



def print_list(list, idx=0):
    if len(list) == idx:
        return 
    print(list[idx])
    print_list(list, idx+1)
heroes = ["spider man", "iron man", "saktiman", "thor", "capton america"]
print_list(heroes)
