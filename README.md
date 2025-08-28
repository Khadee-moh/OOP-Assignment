class Vehicle:
    def move(self):
        print("This vehicle moves in a generic way.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water. 🚤")

# Polymorphism in action
def travel(vehicle):
    vehicle.move()

v1 = Car()
v2 = Plane()
v3 = Boat()

for v in [v1, v2, v3]:
    travel(v)
