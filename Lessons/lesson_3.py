"Принципы ООП"
# number = 3

# number = 5

# print(number)

"Полиморфизм"


# class Animals:
#     def make_sound(self):
#         print("ss")  # не наследуется

# class Cat(Animals):
#     def make_sound(self):
#         print("Meow")

# class Dog(Animals):
#     def make_sound(self):
#         print("GafGAf")

# murka = Cat ()
# murka.make_sound()

# bob = Dog()
# bob.make_sound()


"Инкапсуляция"

class Smartphone:
    def __init__(self, model, color, memory):
        self.model = model  #публичный
        self._color = color  #защищенный 
        self.__memory = memory  #приватный

        " @ - Декоратор "
    @property
    def memory(self):
        return self.__memory
    
    def info (self):  #публичный
        print(f'Phone: {self.model}, {self._color}, {self.__memory}')
        #self.__reset_password ()

    def _messanger(self): #защищенный
        print("whatsApp") 

    def __reset_password (self): #приватный
        print("Sbros password")

    @property
    def reset_password(self):
        return self.__reset_password


samsung = Smartphone("A20", "black", 256)
# # print(samsung.model)
# # print(samsung._color)
# print(samsung.memory)

samsung.info()
# # samsung.get_memory()

# samsung.reset_password()
  

# def sary(func):
#     def tash():
#        print("Hello World")
#        print("Bye")
#        func()
#     return tash 

# @sary
# def add():
#    print(2+2)

# add() 


"Множественное наследование"
class People:  # "Абстрактный класс и Родительский класс"
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    def info (self):
        print(f'Имя - {self.name}, {self.age},{self.hobby} ')

class Father(People):
    def __init__(self, name, age, hobby, job):
        People.__init__(self, name, age, hobby)
        self.job = job

class Mother(People):
    def __init__(self, name, age, hobby, cooking):
        People.__init__(self, name, age, hobby)
        self.cooking = cooking

class Child(Father, Mother):
    def __init__(self, name, age, hobby, job, cooking):
        Father.__init__(self, name, age, hobby, job)
        Mother.__init__(self, name, age, hobby, cooking)   

    def info (self):
        print(f'Имя - {self.name}, {self.age},{self.hobby}, {self.job}, {self.cooking} ')   
    
child = Child("Nurislam", 15, "- ", False, True)
child.info()

    