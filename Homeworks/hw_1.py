# #Задание 1:
# class Fruits:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def info(self):
#         print(f"Название: {self.name}, Цвет: {self.color}, Масса:{self.weight}")

# apple = Fruits("Black Prince", "Red", " 200 gramm")
# apple.info()
# melon = Fruits("Torpeda", "Yellow", "2 kg")
# melon.info()
# peach = Fruits("Nectarine","Light yellow and fiery red hue","150 gramm")
# peach.info()

#Задание 2:
class  Car:
    def __init__(self, model, year, color, fuel):
        self.model = model
        self.year = year 
        self.color = color     
        self.fuel = 0 
    def refuel(self, limitation ):
        self.fuel += limitation
        if self.fuel > 40:
            print("За раз можно пополнить только на 40 литров")
        else:
            print("Ваш бак пополнен на", limitation ,"литров бензина")        
    def drive(self, city, distance): 
        self.distance = distance  
        self.city = city
        print(f'Машина {self.model}, {self.year} года, цвета {self.color} едет в город {self.city} с расстоянием {distance} км')
        a = 10*self.fuel
        b = (distance-a)/ 10
        print(f'С вашим баком вы можете проехать только {a} километров')
        print(f'Чтобы доехать на расстояние {distance} км. Вы должны пополнить ваш бак ещё на {b} литров ')

bmw = Car("BMW X7", "2019", "Ametrin Metallic", 0)
bmw.refuel(40)
bmw.drive("Ош", 600)

super_car = "Car"
SuperCar = "car"