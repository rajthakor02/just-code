# age = int(input("Enter your age = "))

# if(age > 18):
#      print ("You can vote and apply for licence.")

light = "green" 

# if (light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print('wait')
# else:
#     print('go')

marks = float(input("Enter your marks to see your grade = "))

if(marks >= 90):
    print('D')
elif(90>= marks >80):
    print('C')
elif(80>= marks >70):
    print('B')
elif(70>= marks):
    print('A')

age = int(input("Entere your age : "))

if(age>=18):
    if(age>=80):
        print("you cannot drive. you are too old go and watch tv.")
    else:
        print("you can drive.")
else:
    print("you are under age so you cannot drive the car.")