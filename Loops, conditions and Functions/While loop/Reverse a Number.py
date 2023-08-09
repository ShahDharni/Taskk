d=int(input("Enter a number :"))
h=0
while(d>0):
    h=(h*10) + (d%10)
    d=d//10
print("Reverse :",h)