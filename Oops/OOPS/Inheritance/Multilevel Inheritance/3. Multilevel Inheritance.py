class Employees:
    def name(self):
        print("Name of the employee Dharmesh")

class Salary(Employees):
    def salary(self):
        print("Salary of the employee 50000")

class designation(Salary):
    def designation(self):
        print("Designation of the employee Accountant")


a=designation()
a.name()
a.salary()
a.designation()