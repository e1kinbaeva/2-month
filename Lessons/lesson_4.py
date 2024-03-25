"Магические методы - dunder (double underescore) - (методы с двойным подчеркиванием)"
from typing import Any


class Computer:
    def __init__(self, name, ssd):
        self.name = name
        self.ssd = ssd

    # def info (self):
    #     print(f'{self.name}, memory - {self.ssd}')


    def __repr__(self): # Ключовое слово print
        return f'{self.name} memory, - {self.ssd} - repr'
    
    def __str__(self) :
         return f'{self.name}, memory - {self.ssd} - str'
class Macbook(Computer):
    def __init__(self, name, ssd, cpu):
        super().__init__(name, ssd)
        self.cpu = cpu

    def __str__(self) : # print
        return super().__str__() + ", " +f"CPU - {self.cpu}" 
    
    "Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции. "

    def __call__(self): 
        print("Hello world")

    "Магические методы для арифметических действий"

    def __add__(self, other):  # +
        new_ssd = self.ssd+other.ssd
        return Macbook(self.name, new_ssd, self.ssd)
    
    def __sub__(self, other):  # -
        new_ssd = self.ssd-other.ssd
        return Macbook(self.name, new_ssd, self.ssd)
        
    def __mul__(self, other):  # *
        new_ssd = self.ssd*other.ssd
        return Macbook(self.name, new_ssd, self.ssd)
    
    def __floordiv__(self, other):  # //
        new_ssd = self.ssd//other.ssd
        return Macbook(self.name, new_ssd, self.ssd)
    
    def __truediv__(self, other):  # /
        new_ssd = self.ssd/other.ssd
        return Macbook(self.name, new_ssd, self.ssd)
    
    "Магические методы для операторов сравнения"

    def __gt__(self, other): #Больше чем (>)
        return self.ssd > other.ssd
    
    def __lt__(self, other): #Больше чем (<)
        return self.ssd < other.ssd
    
    def __eq__(self, other): #Равно (=)
        return self.ssd == other.ssd
    
    def __ne__(self, other): #Невавно (!=)
        return self.ssd != other.ssd
    
    def __ge__(self, other): #Больше или равно (>=)
        return self.ssd >= other.ssd
    
    def __le__(self, other): # Меньше или равно (<=)
        return self.ssd <= other.ssd

        
mac = Macbook("Macbook pro", 512, "M1" )
# print(mac)
# mac()

mac_2 = Macbook("macbook - air", 512, "M2")

# "Магические методы для арифметических действий"
# print(mac+mac_2)
# print(mac-mac_2)
# print(mac*mac_2)
# print(mac//mac_2)
# print(mac/mac_2)


"Магические методы для операторов сравнения"
print(mac>mac_2)
print(mac<mac_2)
print(mac==mac_2)
print(mac!=mac_2)
print(mac<=mac_2)
print(mac>=mac_2)








# lenovo = Computer("Lenovo", 512 )
# # lenovo.info()
# print(lenovo)



# class Father:
#     def __init__(self,name, height):
#         self.name = name
#         self.height = height
# class Mother:
#     def __init__(self, name, beautiful):
#         self.name = name
#         self.beautiful = beautiful
# class child(Mother,Father):
#     def __init__(self, name, beautiful):
#         super().__init__(name, beautiful)
                 


# child = Child("Ainazik", 154, True)