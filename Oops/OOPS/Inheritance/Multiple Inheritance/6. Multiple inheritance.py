class Calculation1:
    def Addition(self,a,b):
        return a+b
    
class Calculation2:
    def subtraction(self,a,b):
        return a-b
    
class derived(Calculation1,Calculation2):
    def Multiply(self,a,b):
        return a*b
    
d=derived()
print(d.subtraction(34,22))
print(d.Addition(5,2))
print(d.Multiply(8,9))