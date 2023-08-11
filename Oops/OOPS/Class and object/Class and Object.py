## Creating a class and object with class and instance attributes
class Person:
    attr1= "Human"

    def __init__(self,name):
        self.name=name
d=Person("Dharmesh")
a=Person("Dharti")


## Accessing Class attributes
print("Dharmesh is a {}".format(d.__class__.attr1))
print("Dharti is a {}" .format(a.__class__.attr1))
print()

## Accessing Instance attributes
print("My name is {}".format(d.name))
print("My name is {}".format(a.name))