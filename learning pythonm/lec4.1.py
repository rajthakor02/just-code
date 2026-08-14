#q1
dictionary = {
    "cat" : "a small animal ",
    "table" : ["a piece of furniture", "list of facts and figures"]
}
print(dictionary)

#q2
subjects = {"python", "java", "c++","python", "javascript", "java", "python", "java", "c++", "c"}
print(subjects)
print(len(subjects))

#3
marks = {}

x = int(input("Enter physics marks : "))
marks.update({"physics" : x})
y = int(input("Enter chemistry marks : "))
marks.update({"chemistry" : y})
z = int(input("Enter maths marks : "))
marks.update({"maths" : z})

print(marks)