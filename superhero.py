# Base class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.strength_level = strength_level

    def introduce(self):
        print(f"I am {self.name}, and my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power} with strength level {self.strength_level}!")

# Subclass (Inheritance + Polymorphism example for later)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

    # Polymorphic method
    def use_power(self):
        print(f"{self.name} soars into the sky and uses {self.power} from above!")

hero1 = Superhero("Titan", "Super Strength", 95)
hero2 = FlyingSuperhero("Skyfire", "Laser Vision", 88, 300)

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
hero2.fly()
