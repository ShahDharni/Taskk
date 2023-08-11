class Parent:
   def func1(self):
      print("This is the parent class")

class Child(Parent):
   def func2(self):
      print("This is the child class")


d=Child()
d.func1()
d.func2()