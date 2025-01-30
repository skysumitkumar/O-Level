a=int(input("Entre 1st no"))
b=int(input("Entre 2nd no"))
if(a>b):
    print("1st no is greater")
else:
    print("2nd no is greater")

    
    
  
            
a=int(input("Entre 1st no"))

if(a%2==0):
    print("Even no")
else:
    print("Odd no")
    

    
    
Amt=int(input("Eentre amount"))
if(Amt>2000):
              Dis=Amt*20/100
              Net=Amt-Dis
              print("Discount value is",Dis)
              print("Net amount is",Amt)
else:
    Dis=0
    Net=Amt
    print("Discount value is",Dis)
    print("Net amount is",Net)

  


a=int(input("Entre 1st no"))
b=int(input("Entre 2nd no"))
c=int(input("Entre 3rd no"))
if(a>b):
    if(a>c):
        print("1st no is greater")
    else:
        print("3rd no is greater")
else:
    if(b>c):
        print("2nd no is greater")
    else:
        print("3rd no is greater")



a=int(input("Entre 1st no"))
b=int(input("Entre 2nd no"))
c=int(input("Entre 3rd no"))
if(a>b and a>c):
    print("ist no is greater")
elif(b>a and b>c):
    print("2nd no is greater")
else:
    print("3rd no is greater")





day=int(input("Entre the day no"))
if(day==1):
    print("Monday")
elif(day==2):
     print("Tuesday")
elif(day==3):
     print("Wednesday")
elif(day==4):
     print("Thursday")
elif(day==5):
     print("Friday")
elif(day==6):
     print("Saturday")
elif(day==7):
     print("Sunday")
else:
     print("Entre the valid day no")
           
           



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




