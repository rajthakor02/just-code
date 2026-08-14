def pettern(n):
    for i in range(n):
        space = " "*(n-i-1)
        stars = "*"*(2*i+1)
        print(space+stars)

def main():
    n = int(input("Enter the number: "))
    pettern(n)

main()