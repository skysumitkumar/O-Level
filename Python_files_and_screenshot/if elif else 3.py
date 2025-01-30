print("Entre 1 for are of circle")
print("Entre 2 for greater no between two no")
n=int(input())
if(n==1):
    r=int(input("Entre the radius"))
    Area=3.14*r*r
    print("The area of circle is",Area)
elif (n==2):
    a=int(input("Entre 1st no."))
    b=int(input("Entre 2nd no."))
    if(a>b):
        print("1st no is greater")
    else:
        print("2nd no is greater")
else:
    print("go to hell it is a wrong no")
