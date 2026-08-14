#disctionary
info = {
    "key" : "value",
    "college" : "kiran and pallavi patel gandu college",
    "learning" : "coding",
    "age" : 21,
    "an_adult" : True, 
    "marks" : 88.4,
    "subjects" : ["python", "java", "c++"]
} 
print(info)
info["college"] = "KPGU" #overwrite
print(type(info))
print(info["college"])

null_dict = {}
null_dict["name"] = "raj thakor"
print(null_dict)

#nested dictionaries 
student = {
    "name" : "raj thakor",
    "marks" : {
        "chemistry" : 78,
        "physics" : 89,
        "maths" : 83
    }
}
print (student)
print (student["marks"]["chemistry"])# use this for just learning dont use it in projects 
print (list(student.keys()))
print (len(student))
print(student.values())
print(len(student.values()))
print (list(student.values()))
print (student.items())
print(student.get("marks"))#use this one

student.update({"city" : "vadodara"})
print (student)
print (student.get("city"))

#set
collection = {1,2,2,"raj","raj","world"}
print(collection)
print(type(collection))
print(len(collection))

null_set = set() #this shows this is the empty set other wise you do like null_set = {} so it called dictionary

null_set.add(67)
print(null_set)
collection.remove("world")
print(collection)
print(collection.pop())#returns rendom values

print (collection.union(null_set))
print(collection.intersection(null_set))