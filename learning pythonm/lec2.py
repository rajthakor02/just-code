str1 = 'rajthakor02' #for single word use this ''
str2 = "hey i am raj" #use this for "" single lines like this 
str3 = """Transliteration: Kaal Kare So Aaj Kar, Aaj Kare So Ub...
Translation: Tomorrow's work do today, today's work now. If destruction comes in a moment, when will you get it done?
Meaning: Do not put off tasks. Time is unpredictable, so act in the present.""" #just fucking remember when you want to write paragraph like that use """ this 

str1 = "This is a string.\ni am creating it in python." #first line ni niche thi start karva \n ane jo tab space jovtu hoi to \t use karvanu
print(str1)

len = len(str1)
print(len)

#slicing
print(str1[1:4]) #first letter count in but not last 
print(str1[5:])

str2 = "i am coder."
str2 = str2.capitalize()
print(str2.endswith("er."))
# print(str2.capitalize())
print(str2)
# for replace words or alphabets 
print(str2.replace("coder","hacker"))
#count alphabet or word
print(str2.count("am"))