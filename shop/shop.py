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
    """
    pay_rate = 0.85
    all = []
    path_to_csv = os.path.join('items.csv')

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        return repr(f'Item(name={self.__name}, price={self.__price}, quantity={self.__quantity})')

    def __str__(self) -> str:
        return self.__name

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
