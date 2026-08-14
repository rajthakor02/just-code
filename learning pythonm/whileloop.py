# print 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("loop ended.")

#100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended.")

# n = int(input("Enter number : "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

# i = 1
# while i <= 10:
#     print(i * i)
#     i += 1

# heroes = ["Spider Man", "Batman", "Iron Man", "Thor", "Capton Amarica"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1

# numbers = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter the number : "))
# i = 0 
# while i < len(numbers):
#     if numbers[i] == x:
#         print (f"number {x} has in this tuple at index",i)
#         break
#     else:
#         print ("Finding")
#     i += 1
# print("end of loop.")

# i = 0
# while i <= 5:
#     if i == 3 :
#         i += 1
#         continue #skip
#     print (i)
#     i += 1

for i in range(1, 101):
    print(i)