# Multiple Inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

# Creating objects
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# See how rabbit and hawk inherits things from only one parent class but fish inherits things from two parent classes
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()