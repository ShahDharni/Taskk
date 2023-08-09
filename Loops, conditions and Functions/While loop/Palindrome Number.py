d=int(input("Enter a number :"))
a=d
h=0
while(d>0):
    h=(h*10) + (d%10)
    d=d//10
print("Reverse :",h)

if a==h:
    print("It's Palindrome Number")
else:
    print("It's not Palindrome Number")