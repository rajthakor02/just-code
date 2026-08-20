# Check if a given string is a palindrome (ignoring spaces and case sensitivity).
def is_palindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
s = input("Enter a string: ")
if is_palindrome(s):
    print(f"{s} is palindrome.")
else :
    print(f"{s} is not palindrome.")