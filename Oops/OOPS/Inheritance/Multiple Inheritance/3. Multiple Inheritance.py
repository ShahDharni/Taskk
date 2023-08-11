class Father:
    def Driving(self):
        print("Father loves Driving")

class Mother:
    def Cooking(self):
        print("Mother loves Cooking")

class Son(Father,Mother):
    def Playing(self):
        print("Son loves Playing")


a=Son()
a.Driving()
a.Cooking()
a.Playing()