#ООП- Объектно ориентированное программирование
"DRY - Don't Repeat Yourself"

class Car:  #чертеж или щаблон
    wheels = 4
    #"__init__ - конструктор"
    #"self - сам объект"
    def __init__(self, model, color, max_speed):
        #"self.model- Атрибут/ Свойство/ поле объекта"
        self.model = model
        self.color = color
        self.is_start = False
        self.tank = 0
        self.max_speed = max_speed

    def info (self):
        print(self.model, self.color)

    def start(self):
        self.is_start = True
        print("Машина завелась")

    def stop(self):
        self.is_start = False
        print("Машина  приглушена")
    
    def drive(self, speed):
        if self.is_start == True and self.tank > 0 :
            if speed < self.max_speed:
                print(f"машина {self.model} поехала со скоростью {speed} км час")
            else:
                print("Вы превысили допустимую скорость машины")
        else:
            print("Машина не заведена или нет топливо")
        
    def fill(self, value_tank):
        self.tank += value_tank


mercedes = Car("Mers", "black", 320)
mercedes.info()
mercedes.fill(100)
mercedes.start()
mercedes.drive(100)
mercedes.stop()



# bmw = Car("BMW_$", "White")
# print(bmw.model, bmw.color)
# bmw.info()
# bmw.drive()





print("Hello worl.d")

