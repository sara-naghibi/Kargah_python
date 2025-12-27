from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Mostatil(Shape):
    def __init__(self, arz, ertefa):
        self.arz = arz
        self.ertefa = ertefa

    def calculate_area(self):
        return self.arz * self.ertefa

    def calculate_perimeter(self):
        return 2 * (self.arz + self.ertefa)

class Dayere(Shape):
    def __init__(self, shoa):
        self.shoa = shoa

    def calculate_area(self):
        return 3.14159 * self.shoa * self.shoa

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.shoa

m1 = Mostatil(10, 5)
d1 = Dayere(7)

list_shekl_ha = [m1, d1]

for shekl in list_shekl_ha:
    print(shekl.calculate_area())
    print(shekl.calculate_perimeter())
