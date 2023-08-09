k=int(input("Enter a number :"))
i=1
while(k>0):
    b=1
    while b<i:
        print("_",end="")
        b=b+1
    j=1
    while j<=(k*2)-i:
        print("*",end="")
        j=j+1

    print()
    k=k-1
    i=i+1

