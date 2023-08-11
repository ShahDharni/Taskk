class Person():
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    
class Father(Person):
    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age=age
    def getAge(self):
        return self.age
    
class Child(Father):
    def __init__(self,name,age,location):
        Father.__init__(self,name,age)
        self.location=location
    def getLocation(self):
        return self.location


d=Child("Dharmesh",23,"Ahmedabad")
print(d.getName())
print(d.getAge())
print(d.getLocation())