# The super() function is used to give access to methods and properties of a parent or sibling class. 
class Person():
    def __init__(self):
        print("Person -- Hi")
    
    def age(self,a):
        print("Printing the age :",a)

class Father(Person):
    def __init__(self):
        print("Father --Hi")
        super().__init__()


    def age(self,a):
        print("Printing the age of Father :",a)
        super().age(a-1)

class Mother(Father):
    def __init__(self):
        print("Mother -Hi")
        super().__init__()



    def age(self,a):
        print("Printing the age of Mother :",a)
        super().age(a+5)


o=Mother()
o.age(30)