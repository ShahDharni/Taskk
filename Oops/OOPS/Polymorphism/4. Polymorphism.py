class Bird:
    def intro(self):
        print("There are different kinds of birds")

    def flight(self):
        print("Most of the Birds can fly but some cannot")

class parrot(Bird):
    def flight(self):
        print("Parrots can fly")

class penguins(Bird):
    def flight(self):
        print("Penguins cannot fly but they are so cute")

obj_bird= Bird()
obj_parr=parrot()
obj_peng=penguins()


obj_bird.intro()
obj_bird.flight()

obj_parr.intro()
obj_parr.flight()

obj_peng.intro()
obj_peng.flight()
