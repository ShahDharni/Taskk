class Father:
    def func1(self):
        print("I am Father")


class Son(Father):
    def func2(self):
        print("I am Son")



a=Son()
a.func1()
a.func2()