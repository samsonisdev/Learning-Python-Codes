class Car:

    color = None

class Motorbike:

    color = None

def change_color(vehicle, color):

    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike = Motorbike()

change_color(car_1, "red")
change_color(car_2, "yellow")
change_color(car_3, "blue")
change_color(bike, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike.color)