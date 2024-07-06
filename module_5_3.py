from random import randint  # импортируем модуль для генерации случайных чисел


class House:

    def __init__(self, name, number_of_floors: int):  # указываем атрибуты
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):  # создаем метод
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

    def __add__(self, value):
        if isinstance(value, (int, House)):
            return self.number_of_floors + value

        return print(f'нельзя сложить {self.number_of_floors} и {value}')

    def __iadd__(self, value):
        if isinstance(value, (int, House)):
            nf = value if isinstance(value, int) else value.number_of_floors
            self.number_of_floors += nf
            return self

        return print(f'нельзя сложить {self.number_of_floors} и {value}')

    def __radd__(self, value):
        if isinstance(value, (int, House)):
            return self.number_of_floors + value

        return print(f'нельзя сравнить {self.number_of_floors} и {value}')

    def __eq__(self, other):  # Равенство
        if isinstance(other, (int, House)):
            return self.number_of_floors == other

        return print(f'нельзя сравнить {self.number_of_floors} и {other}')

        # if not isinstance(other, House):
        #     return print(f'нельзя сравнить {self.number_of_floors} и {other.number_of_floors}')
        # else:
        #     return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # Меньше
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        return print(f'нельзя сравнить {self.number_of_floors} и {other}')

    def __le__(self, other):  # Меньше или равно
        if isinstance(other, (int, House)):
            return self.number_of_floors <= other.number_of_floors

        return print(f'нельзя сравнить {self.number_of_floors} и {other.number_of_floors}')

    # def __gt__(self, other): # Больше
    #     if isinstance(other, House) and isinstance(other.number_of_floors, int):
    #         return self.number_of_floors > other.number_of_floors
    #     else:
    #         return print(f'нельзя сравнить {self.number_of_floors} и {other.number_of_floors}')


elbrus = House('ЖК Эльбрус', 30)


dom = House('Дом в деревне', 3)

elbrus.go_to(randint(1, 100))
dom.go_to(randint(1, 100))
# __len__
print(f' всего этажей в {elbrus} {len(elbrus)}')
print(f' всего этажей в {dom} {len(dom)}')
# __str__
print(f' Название комплекса {elbrus}')
print(f' Название комплекса {dom}')
# равенство
print(f' равенство {elbrus.number_of_floors} = {dom.number_of_floors} : {elbrus == dom}')
# меньше
print(f' меньше {elbrus.number_of_floors} < {dom.number_of_floors} : {elbrus < dom}')
# меньше или равно
print(f' меньше или равно {elbrus.number_of_floors} <= {dom.number_of_floors} : {elbrus <= dom}')
# Больше
print(f' Больше {elbrus.number_of_floors} > {dom.number_of_floors} : {elbrus > dom}')
# Больше или равно
print(f' больше или равно {elbrus.number_of_floors} => {dom.number_of_floors} : {elbrus >= dom}')
# Не равно
print(f' не равно {elbrus.number_of_floors} != {dom.number_of_floors} : {elbrus != dom}')
#  add
dom.number_of_floors = dom.number_of_floors + 27
print(f' Название {dom} количество этажей {len(dom)}')
print(f' равенство {elbrus.number_of_floors} = {dom.number_of_floors} : {elbrus == dom}')
# iadd
dom.number_of_floors += 10
print(f' Название {dom} количество этажей {len(dom)}')
# radd
dom.number_of_floors = 10 + dom.number_of_floors
print(f' Название {dom} количество этажей {len(dom)}')
print(elbrus == 30)
print(elbrus < 30)
