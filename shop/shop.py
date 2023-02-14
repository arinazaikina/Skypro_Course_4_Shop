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

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return repr(f'Item({self.__name}, {self.__price}, {self.__quantity})')

    def __str__(self):
        return self.__name

    @property
    def name(self) -> str:
        """Геттер. Возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Сеттер. Устанавливает название товара"""
        self.__name = name

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