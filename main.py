from turtle import speed
class All_cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return "{} {} start go, speed =  {}km".format(self.color, self.name, self.speed)
    def stop(self):
        return "{} {} start stop, speed = {}km".format(self.color, self.name, int(self.speed) %int(self.speed)) 
    def turn_right(self):
        return "{} {} move right, speed = {}km".format(self.color, self.name, int(self.speed) -10) 
    def turn_left (self):
        return "{} {} move left, speed = {}km".format(self.color, self.name, int(self.speed) -10)

class TownCar(All_cars):
    def __init__(self, speed, color, name, is_police):
        All_cars.__init__(self, speed, color, name, is_police)   
First_car = [
    TownCar("200", "pink", "peugeot", False),
    TownCar("220", "white", "volkswagen", False)
] 
class SportCar(All_cars):
    def __init__(self, speed, color, name, is_police):
        All_cars.__init__(self, speed, color, name, is_police) 
Second_car = [
    SportCar("290", "black", "porshe", False),
    SportCar("320", "white", "maseratti", False)
] 
class WorkCar(All_cars):
    def __init__(self, speed, color, name, is_police):
        All_cars.__init__(self, speed, color, name, is_police) 
Third_car = [
    WorkCar("400", "purple", "daewoo lanos", False),
    WorkCar("160", "green", "renault", False)
] 
class PoliceCar(All_cars):
    def __init__(self, speed, color, name, is_police):
        All_cars.__init__(self, speed, color, name, is_police) 
Fourth_car = [
    PoliceCar("205", "blue", "prius", True),
    PoliceCar("120", "blue", "bobik", True)
] 
voice = int(input("Town car = 1, Sport car = 2, Work car = 3, Police car = 4: "))
move = int(input("Go = 1, stop = 2 or turn(l = 3 or r = 4): "))
if voice == 1:
    a = First_car
elif voice == 2:
    a = Second_car
elif voice == 3:
    a = Third_car
elif voice == 4:
    a = Fourth_car
def carstown():
    if move == 1:
        for All_cars in (a):
            print("{}".format(All_cars.go()))
    if move == 2:
        for All_cars in (a):
            print("{}".format(All_cars.stop()))
    if move == 3:
        for All_cars in (a):
            print("{}".format(All_cars.turn_right()))
    if move == 4:
        for All_cars in (a):
            print("{}".format(All_cars.turn_left()))
carstown()
