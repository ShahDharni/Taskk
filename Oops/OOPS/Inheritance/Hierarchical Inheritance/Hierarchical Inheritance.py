class classA():
    def display(self):
        print("In class A")

class classB(classA):
    def display(self):
        classA.display(self)
        print("In class B")
 
class classC(classA):
     def display(self):
        classA.display(self)
        print("In class C")

class classD(classA):
     def display(self):
        classA.display(self)
        print("In class D")


x=classB()
y=classC()
z=classD()
x.display()
y.display()
z.display()