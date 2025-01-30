s="python"
for x in s:
    print(x)



str=input("entre a string value:")
i=0
for x in str:
    print(i, "index is:",x)
    i=i+1



#range (start , stop[ , step)




print("using one argument in range")
for i in range(6):
    print(i,end=', ')
               




print("using one argument in range")
for i in range(1,20,2):
    print(i,end=', ')





for i in range(2):
    for j in range(2):
        print("i=",i,"j=",j)




n= int(input("entre no of rows:"))
for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)




n=int(input("entre no of rows:"))
for i in range(1,n+1):
    print(" "*(n-1),end="")
    print("*" * i)



for row in range(6):
    for col in range (6):
        if col==0 or col ==5 or (row == col and col>0 and col<5):
            print("*",end="")
        else:
                print(end=" ")
    print()
