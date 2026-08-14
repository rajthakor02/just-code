#WAP 1 to chech if a number is ever or odd.
num = int(input("Enter any number you want to know it is ever or odd : "))
if(num % 2) == 0:
    print("Entered number is even.")
else:
    print("Emtered number is odd.")

#WAP 2 to find the greatest of 3 numbers entered by the user

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
n3 = int(input("Enter the third number : "))

if n1 >= n2 and n1 >= n3:
    print (n1,"is the biggest number you has entered.")
elif n2 >= n1 and n2 >= n3:
    print (n2,"is the biggest number you has entered.")
else:
    print (n3,"is the biggest number you has entered.")

#WAP 3 to check if a number is a multiple of 7 or not.

num2 = int(input("Enter number : "))

if (num2 % 7) == 0:
    print(f"{num2} is the multiple of 7.")
else:
    print(f"{num2} is not multiple of 7.")