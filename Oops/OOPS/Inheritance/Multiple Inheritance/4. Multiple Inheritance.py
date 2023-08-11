class Car:
    def Benz(self):
        print("This is the Benz car")

class Bike:
    def TVS_Raider(self):
        print("This is the TVS Raider Bike")

class Bus:
    def Volvo(self):
        print("This is the Volvo Bus")


class Truck:
    def Eicher(self):
        print("This is the Eicher Truck")
   

class Plane:
    def Indigo(self):
        print("This is the Indigo Plane")


class Transport(Car,Bike,Bus,Truck,Plane):
    def main(self):
        print("This is the main class")


d=Transport()
d.Benz()
d.Eicher()
d.Indigo()
d.Volvo()
d.TVS_Raider()















































#   bike=bmw
# bus=volvo
# truck = eicher
# plane=indigo      