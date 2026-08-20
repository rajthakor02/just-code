#Reverse a string manually without using built-in slicing ([::-1]) or reversed().
# def reverse_string(text):
#     reversed_text = ""
#     for char in text:
#         # Prepend the character to the existing string
#         reversed_text = char + reversed_text  
#     return reversed_text

# # Example usage:
# print(reverse_string("hello"))  # Output: "olleh"
def reversestring(s):
    reverse_string = "" 
    for chr in s:
        reverse_string = chr + reverse_string

    return reverse_string
print(reversestring("raj thakor"))