def pettern1():
    for i in range(1,6):
        print(f"*"*i)

def pettern2():
    for i in range(5,0,-1):
        print(f"*"*i)

def pettern3():
    n = 5  # Number of rows
    for i in range(0,n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

def selection():
    while True:
        slt = int(input("Select the option: "))

        if slt == 1:
            pettern1()
        elif slt == 2:
            pettern2()
        elif slt == 3:
            pettern3()
        elif slt == 4:
            break
        else:
            print("Enter valid integer.")

def main():
    menu = ("""
1)
*
**
***
****
*****\n"""
            """2)
*****
****
***
**
*\n"""
"""3)
    *
   ***
  *****
 *******
*********"""
    )
    print(menu)
    selection()
main()