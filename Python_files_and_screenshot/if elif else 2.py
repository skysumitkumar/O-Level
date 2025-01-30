a=int(input("Entre 1st no"))
b=int(input("Entre 2nd no"))
print("Entre 1 for add")
print("Entre 2 for sub")
print("Entre 3 for div")
print("Entre 4 for mul")
n=int(input())
if (n==1):
    c=a+b
    print("Addition is",c)
elif (n==2):
    c=a-b
    print("Subtration is",c)
elif (n==3):
    c=a/b
    print("Division is",c)
elif (n==4):
    c=a*b
    print("Multiplication is",c)
else:
    print("Entre a valid no.")

