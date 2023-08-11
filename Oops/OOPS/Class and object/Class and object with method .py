## Creating Class and Object with methods

class Person:
    attr= "Human"

    def __init__ (self,name):
        self.name=name

    def listen(self):
        print("My name is {}".format(self.name))

d=Person("Dharmesh")
a=Person("Dharti")

## Accessing class methods
d.listen()
a.listen()