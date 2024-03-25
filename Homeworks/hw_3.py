class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu (self):
         return self.__cpu
    @property
    def memory(self):
         return self.__memory

    def __make_computations (self):
        print(f'Сложение: {self.cpu + self.memory}')
        print(f'Вычитание: {self.cpu - self.memory}')
        print(f'Умножение: {self.cpu * self.memory}')
        print(f'Деление: {self.cpu / self.memory}')
        
    @property
    def make_computations(self):
        return self.__make_computations
    
class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        Computer.__init__(self, cpu, memory)
        self.__memory_card = memory_card

    @property
    def memory_card(self):
        return self.__memory_card
    
    def info(self):
        print(f'Центральное обрабатывающее устройство: {self.cpu} Ггц , Память: {self.memory}Гб,  Карта памяти: {self.memory_card} Гб')
        self.make_computations()
laptopq = Laptop(2.6, 512, 2 )
laptopq.info()


        
   