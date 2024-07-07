# Method Chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self
# Adding 'return self' to each method so that we can call multiple methods in a single line
class Car:

    def turn_on(self):
        print("You turn on the engine")
        return self
    def drive(self):
        print("You start driving")
        return self

    def brakes(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the car")
        return self

# Creating an object
car = Car()

# this a long way to call multiple methods
# car.turn_on()
# car.drive()
# car.brakes()
# car.turn_off()

# instead:
car.turn_on().drive().brakes().turn_off()
