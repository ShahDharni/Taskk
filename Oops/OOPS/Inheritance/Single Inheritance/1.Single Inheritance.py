## Single Inheritance


## Parent Class
class Person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number

    def display(self):
        print(self.name)
        print(self.id_number)       
        
    def details(self):
        print("My name is {}".format(self.name))
        print("My id_number is {}".format(self.id_number))

## Child Class
class Employee(Person):
    def __init__(self,name,id_number,salary,City):
        self.salary=salary
        self.City=City

        Person.__init__(self,name,id_number)
     
    def details(self):
        print("My name is {}".format(self.name))
        print("My id_number is {}".format(self.id_number))
        print("My salary is {}".format(self.salary))
        print("My City is {}".format(self.City))


d=Employee("Dhwani",23,50000,"Ahmedabad")
d.details()
d.display()