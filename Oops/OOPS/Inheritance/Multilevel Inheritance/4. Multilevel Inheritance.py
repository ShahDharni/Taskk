class Family:
    def show_family(self):
        print("This is our Family")

class Father(Family):
    fathername=" "
    def Father(self):
        print(self.fathername)

class Mother(Family):
    mothername=" "
    def Mother(self):
        print(self.mothername)


class Son(Father,Mother):
    def show_parent(self):
        print("Father :",self.fathername)
        print("Mother :",self.mothername)

a=Son()
a.fathername="Aarav"
a.mothername="Anika"
a.show_family()
a.show_parent()
