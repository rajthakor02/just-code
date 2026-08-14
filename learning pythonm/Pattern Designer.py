def pettern1(n):
    for i in range(1, n+1):
        print("*"*i)

def pettern2(n):
    for i in range(n,0,-1):
        print("*"*i)

def pettern3(n):
    for i in range(1,n+1):
        spaces = n - i
        stars = (2*i)-1
        print(" "*spaces+"*"*stars)
        

def main():
    print("""there are three pettern which one you want to print select first by their number.
    1)
*
**
***
****
*****

2)
*****
****
***
**
*

3)
    *
   ***
  *****
 *******
*********""")
    choices = int(input("Enter your choice : "))
    selectpettern(choices)
    
def selectpettern(choices):
    if choices == 1:
        n = int(input("Enter number:"))
        pettern1(n)
    if choices == 2:
        n = int(input("Enter number:"))
        pettern2(n)
    if choices == 3:
        n = int(input("Enter number:"))
        pettern3(n)
main()
