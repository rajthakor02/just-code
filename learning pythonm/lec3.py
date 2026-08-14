#tuple and list 
# movies = []

# mov1 = input("Enter 1st movie : ")
# mov2 = input("Enter 2nd movie : ")
# mov3 = input("Enter 3rd movie : ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print (movies)

#one other way
# movies = []

# mov = input("Enter 1st movie : ")
# movies.append(mov)
# mov = input("Enter 2nd movie : ")
# movies.append(mov)
# mov = input("Enter 3rd movie : ")
# movies.append(mov)

# print (movies)

#second and best way 
movies = []

movies.append(input("Enter 1st movie : "))
movies.append(input("Enter 2nd movie : "))
movies.append(input("Enter 3rd movie : "))

print (movies)

# wap check palindrome
list1 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("palindrome")
else:
    print("non palindrome")

#wap to count the number of student with the "A" grade in the following tuple 
grade = ("C","D","A","A","B","B","A")
print(f"""the number of student with the "A" grade in the following is {grade.count("A")}""")

#wap 