from random import randint # импортируем модуль для генерации случайных чисел
class House:

    def __init__(self, name, number_of_floors): # указываем атрибуты
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor): # создаем метод
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'В {self.name} Этажа {new_floor} не существует')
        else:
            print(f'В {self.name} Переходим на {new_floor} этаж')
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name

    # def __eq__(self, other): # Равенство
    #     if isinstance(other, House) and isinstance(other.number_of_floors, int):
    #         return self.number_of_floors == other.number_of_floors
    #     else:
    #         return print(f'нельзя сравнить {self.number_of_floors} и {other.number_of_floors}')
    #
    def __lt__(self, other): # Меньше
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            return print(f'нельзя сравнить {self.number_of_floors} и {other.number_of_floors}')
    #
    def __le__(self, other): # Меньше или равно
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        else:
            return print(f'нельзя сравнить {self.number_of_floors} и {other.number_of_floors}')
    #
    # def __gt__(self, other): # Больше
    #     if isinstance(other, House) and isinstance(other.number_of_floors, int):
    #         return self.number_of_floors > other.number_of_floors
    #     else:
    #         return print(f'нельзя сравнить {self.number_of_floors} и {other.number_of_floors}')

elbrus = House('ЖК Эльбрус', 30)
dom = House('Дом в деревне', 3)
elbrus.go_to(randint(1, 100))
dom.go_to(randint(1, 100))
#__len__
print(f' всего этажей в {elbrus} {len(elbrus)}')
print(f' всего этажей в {dom} {len(dom)}')
#__str__
print(f' Название комплекса {elbrus}')
print(f' Название комплекса {dom}')
# равенство
print(elbrus == dom)
# меньше
print(elbrus < dom)
# меньше или равно
print(elbrus <= dom)
# Больше
print(elbrus > dom)
# Больше или равно
print(elbrus >= dom)
# Не равно
print(elbrus != dom)