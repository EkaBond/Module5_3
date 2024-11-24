class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor >= 1 and new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.')
                

# Блок выше это с предыдущих модулей. 5_1 и 5_2, комментарии были оставлены в предыдцщих ДЗ
# Блок ниже, это текущее ДЗ. С этими функциями проблем не возникло, они делались по шаблону урока.
# все эти функции производят сравнения разных видов (равно, больше, меньше) и выдают
# True если это так и False если ложно. Напр: если кол-во этажей равно, выдаст True, если нет False

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def  __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def  __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

# Данные ниже операторы производят действие сложение и возвращают результат.
#   __add__ складывает значения объектов, т.к. этим значением может быть не только целое число, а мы хотим
#    в нашем случаеприбавить к нашим этажам еще этажи, то нам нужно проверить, является ли передаваемые
#    данные числом. он так же может сложить строки, слепив их и списки и т.д. поэтому нужно помнить,
#    что у нас в дано и/ или вписывать условия проверки
#   __iadd__ складывет целочисленные значения. т.к. мы внутри этой функции возвращаем вункцию __add__, то
#    проверку можно уже не делать
#   __radd__ дополняет метод __add__ когда левый операнд не имеет метода add
#   или когда его метод add не знает, как обработать правый операнд.

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__