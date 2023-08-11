## Area of rectangle using Multiple Inheritance

class length():
    l=0
    def length(self,l):
       return self.l

class breadth():
    b=0
    def breadth(self,b):
       return self.b

class rect_area(length,breadth):
    def area(self):
        print("Area of Rectangle is " + " " + str(self.l) + " " + "units and breadth" + " " + str(self.b) + " " + " " + "units is" + " " + str(self.l * self.b) + " " + "sq units")

a=rect_area()
a.l=int(input("Enter length :"))
a.b=int(input("Enter Breadth :"))
a.area()