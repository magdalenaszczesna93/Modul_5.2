class Car:
   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color
       # Variables 
       self._current_speed = 0
   def __str__(self):
          return f"{self.color} {self.make} {self.model_name}"
   def accelerate(self, step=10):
       self.current_speed += step
   def decelerate(self, step=10):
       self.current_speed -= step

   @property
   def current_speed(self):
       return self._current_speed 
   @current_speed.setter
   def current_speed(self, value):
       if value <= self.top_speed:
           self._current_speed = value
       else:
           raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car.current_speed = 100
print(car.current_speed)

class DieselEngine:
    def tank(slef, how_many=100):
        print(f'Adding {how_many} liters of Diesel')

class PetrolEngine:
    def tank(self, how_many=20):
        print(f'Adding {how_many} liters od Petrol')

class Truck(Car, DieselEngine):
    def __init__ (self, max_load, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_load = max_load

truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)

class SportCar(Car, PetrolEngine):
    pass

porsche = SportCar(make='Porsche', model_name='911', color='Red', top_speed=250)
    
truck.tank()
porsche.tank()

import this




