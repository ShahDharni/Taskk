# if condition :-
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
if a>b :
    print("a is greater")

# else condition :-
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
if a>b :
    print("a is greater")
else:
    print("b is greater")


# if-elif condition :-
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
if a>b :
    print("a is greater")
elif a<b:
    print("b is greater")
else:
    print("Equal")





## Short Hand If :-
if a>b : print("a is greater than b")


## Short Hand if-else :-
a = 2
b = 330
print("A") if a > b else print("B")

## 2
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")




## Nested If else :-
x=56
if x>50:
 print("x is greater than 50")
 if x < 100:
     print("Also greater than 100")
 else:
     print("Not greater than 100")

else:
    print("Not greater than 50")
