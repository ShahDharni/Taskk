## Multiple Inheritance :-

class A():
    def A(self):
        print("This is class A")

class B():
    def B(self):
        print("This is class B")

class C(A,B):
    def C(self):
        print("This is the class C inherits from A and B")


O=C()
O.A()
O.B()
O.C()



