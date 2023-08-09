def my_func():
    print("Hello World")

my_func()



## Arguments
def my_func(fname):
    print("Hello" + " " + fname)

my_func("Om")
my_func("Rudra")
my_func("Shivay")

print()
## Passing List as an arguments
def my_func(d):
   for x in students:
      print(x)
   
students=["Om","Rudra"]
print("Passing list as an arguments ")
my_func(students)


## Recursion
def recursion(d):
  if(d > 0):
    result = d + recursion(d - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
recursion(2)


## User Defined

def evenodd(x):
   if (x%2)==0:
      print("even")
   else:
      print("odd")

y=int(input("Enter number :"))
evenodd(y)
      

## Built-in functions


# 1. delattr

class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')


# 2. zip

a = ("Om", "Rudra", "Shivay")
b = ("Jay", "Arjun", "Aariv")

x = zip(a, b)
print(x)



## Lambda Function
def my_func(n):
   return lambda a: a*n
d=my_func(12)
d1=my_func(6)
print(d(11))
print(d1(11))