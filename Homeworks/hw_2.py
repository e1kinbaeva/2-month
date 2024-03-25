class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(self.fullname , self.age, self.is_married )
class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience
        self.salary = salary
        self.salary = 0
    def introduce_myself(self):
        print( "Учитель:",self.fullname , ", Возраст:",self.age,", Семейное положение:", self.is_married,", Опыт работы:", self.experience, "лет")
    def CountSalary (self, countsalary):
        self.salary += countsalary
        print(f"Первоначальная сумма зарплаты составляет {self.salary}.","Бонус за опыт работы составляет", int(self.experience* 3000), ". Всего зарплата :", int(self.salary+(self.experience* 3000)),"сомов") 

teacher = Teacher("Matikeev Bilal", 55, "Женат" , 30, 30000)
teacher.introduce_myself()
teacher.CountSalary(20000)