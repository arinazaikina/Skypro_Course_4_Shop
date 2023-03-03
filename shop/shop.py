import csv
import os.path


class Item:
    """
    Базовый класс, описывающий Товар
    Attrs:
        name (str): передаётся название товара
        price (float): передаётся цена товара
        quantity (int): передаётся количество товара
        pay_rate (float): уровень цен с учётом скидки
        all: список экземпляров класса
        path_to_csv: путь к файлу, на основе которого можно создать
        экземпляры класса
    """
    pay_rate = 0.85
    all = []
    path_to_csv = os.path.join('items.csv')

    def __init__(self, name, price, quantity):
        self.__name = name
        if price < 0 or quantity < 0:
            raise AttributeError('Цена и количество товара не могут быть меньше 0')
        else:
            self.__price = price
            self.__quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        return f'Item(name={self.__name}, price={self.__price}, quantity={self.__quantity})'

    def __str__(self) -> str:
        return self.__name

    def __add__(self, other):
        """Сложение по количеству товара"""
        if not isinstance(other, Item):
            raise TypeError('Правый операнд должен быть объектом класса Item или объектом наследника класса Item')
        return self.__quantity + other.__quantity

    @property
    def name(self) -> str:
        """Геттер. Возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Сеттер. Устанавливает название товара.
        Если длина названия превышает 10 символов, выбрасывается исключение
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

    @property
    def price(self) -> float:
        """Геттер. Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер. Устанавливает цену товара"""
        price = round(price, 2)
        self.__price = price

    @property
    def quantity(self) -> int:
        """Геттер. Возвращает количество товара"""
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        """Сеттер. Устанавливает количество товара"""
        self.__quantity = quantity

    def calculate_total_price(self):
        """Получить общую стоимость конкретного товара в магазине"""
        total_cost = self.__price * self.__quantity
        return total_cost

    def apply_discount(self):
        """Применить установленную скидку для конкретного товара"""
        self.price = round(self.price * self.pay_rate, 2)
        return self.price

    @staticmethod
    def get_price(num: str):
        """
        Проверяет является ли число целым
        :param num: число str
        """
        if '.' in num:
            if num.split('.')[1] == '0':
                return int(num.split('.')[0])
            return float(num)
        return int(num)

    @classmethod
    def instantiate_from_csv(cls, path: str) -> None:
        """
        Альтернативный способ создания объектов-товара.
        Метод считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла.
        :param path: путь к файлу с данными.
        """

        with open(path, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                cls(name=row['name'], price=cls.get_price(row['price']), quantity=int(row['quantity']))


class Phone(Item):
    """
    Класс, описывающий Смартфон
    Родительский класс - класс Item
    Attrs:
        name (str): передаётся название смартфона
        price (float): передаётся цена смартфона
        quantity (int): передаётся количество смартфонов
        sima_cards_amount (int): передаётся количество сим-карт в смартфоне
    """

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim not in [1, 2]:
            raise AttributeError('Количество физических SIM-карт должно быть равно 1 или 2.')
        else:
            self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return super().__repr__().replace('Item', 'Phone').replace(')', f', number_of_sim={self.__number_of_sim})')

    @property
    def number_of_sim(self) -> int:
        """Геттер. Возвращает количество сим-карт в смартфоне"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) -> None:
        """
        Сеттер. Устанавливает количество сим-карт в смартфоне.
        Если количество сим-карт не 1 или не 2, выбрасывается исключение
        """
        if number_of_sim in [1, 2]:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть равно 1 или 2.')


class MixinKeyboardLayout:
    """
    Класс-миксин для хранения и изменения раскладки клавиатуры.
    Attrs:
        language (str): язык. Поддерживается два языка: 'EN' и 'RU'.
        Язык по умолчанию (при инициализации) - английский 'EN'.
    """

    def __init__(self, *args, **kwargs):
        self.__language = 'EN'
        super().__init__(*args, **kwargs)

    @property
    def language(self):
        """Геттер. Возвращает язык клавиатуры."""
        return self.__language

    def change_lang(self):
        """Изменяет язык клавиатуры"""
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class KeyBoard(MixinKeyboardLayout, Item):
    """
    Класс, описывающий Клавиатуру
    Родительский класс - класс Item.
    Миксин-класс - класс MixinKeyboardLanguage (хранит и изменяет раскладку)
    Attrs:
        name (str): передаётся название клавиатуры
        price (float): передаётся цена клавиатуры
        quantity (int): передаётся количество клавиатур
    """

    def __repr__(self) -> str:
        return super().__repr__().replace('Item', 'KeyBoard')
