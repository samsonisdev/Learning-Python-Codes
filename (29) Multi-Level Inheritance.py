# Multi-Level Inheritance = when a derived child class inherits everything from another
#                           derived child class

# Here, 'Organism' is the great parent class, then Animal is its child class and then dog is Animal's child class or Organisms grand child. This works like a hierarchy
class Organism:

     alive = True

class Animal(Organism):

    def eat(self):
        print("This animal eats")

    def sleep(self):
        print("This animal sleeps")

class Dog(Animal):

    def bark(self):
        print("This dog barks")

# Now creating objects
dog = Dog()
animal = Animal()

print(dog.alive) # see how the dog inherits the attributes from the great parent class 'Organism'
dog.eat()
animal.sleep()
dog.bark()