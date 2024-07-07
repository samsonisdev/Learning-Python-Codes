
# OOP (Object-Oriented Programming) = By OOP we can create representation of real life objects by assigning classes.
# Classes are like a blueprint for objects
# An object has two main things:
# 1) Data/Attribute = Features of an object like a watch's shape, color, material, etc.
# 2) Methods/Functions = Things that an object can do, like a watch can show time, change time etc

class Car:

    wheels = 4 # class variable ( look at the end for explanation)

    # attributes
    def __init__(self, make, model, year, color):
        self.make = make        # instance variable
        self.model = model      # instance variable
        self.year = year        # instance variable
        self.color = color      # instance variable

    # methods
    def drive(self):
        print("This " + self.model + " is driving!")

    def stop(self):
        print("This " + self.model + " has stopped!")

# Creating objects car_1 and car_2
car_1 = Car("Toyota", "Supra", 2024, "Black")
car_2 = Car("Honda", "Civic", 2023, "Blue")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_1.stop()


Car.wheels = 4 # by accessing the class variable and changing to a different number, it'll affect car_1 and car_2
print(Car.wheels)

car_2.wheels = 2 # but if we access the object, we can change only the object's value, and it won't affect any other objects in the class Car
print(car_2.wheels)
