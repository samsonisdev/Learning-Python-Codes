# Prevents a user from creating an object of that class
# and compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

# Basically when we don't want the user to create an object of a class, we use abstract method
# Like we're designing a game, and we want the user to only make an object of car or motorbike but not the vehicle cuz we specified the vehicles 'Car' and 'Motorbike'

# if we remove the abstract method, we can still make an object of that class (we don't want that to happen) so it's better to add at least one abstract method in a class in order to have the user not be able to make an object of that class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car has stopped")

class Motorbike(Vehicle):

    def go(self):
        print("You ride the motorbike")

    def stop(self):
        print("This motorbike has stopped")

# Creating objects
# vehicle = Vehicle()
car = Car()
motorbike = Motorbike()

car.go()
motorbike.go()
car.stop()
motorbike.stop()