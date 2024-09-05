import inspect

def introspection_info(obj):
    dict_ = {}
    dict_.update({'Тип объекта:': type(obj)})
    list_attr, list_meth = [], []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if not callable(attr):
            list_attr.append(attr_name)
        else:
            list_meth.append(attr_name)
    dict_.update({'Атрибуты объекта:': list_attr})
    dict_.update({'Методы объекта:' : list_meth})
    dict_.update({'Модуль, к которому объект принадлежит:': inspect.getmodule(obj)})
    return dict_

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
               print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self + value

    def __radd__(self, value):
        return self + value


if __name__ == '__main__':
    number_info = introspection_info(42)
    for key, value in number_info.items():
        print(key, value)

    func_ = introspection_info(get_multiplied_digits)
    for key, value in func_.items():
        print(key, value)

    h1 = House('ЖК Эльбрус', 10)
    res = introspection_info(h1)
    for key, value in res.items():
        print(key, value)

    res2 = introspection_info(House)
    for key, value in res2.items():
        print(key, value)








