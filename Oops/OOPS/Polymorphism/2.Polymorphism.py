class Tomato:
    def type(self):
        print("Vegetable")
    def color(self):
        print("red")

class Apple:
    def type(self):
        print("Fruits")
    def color(self):
        print("red") 

def func(obj):
    obj.type()
    obj.color()

obj_tomato=Tomato()
obj_apple=Apple()
func(obj_tomato)
func(obj_apple)