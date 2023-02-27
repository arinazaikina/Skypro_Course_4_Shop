import os

import pytest

from shop.shop import Item


def test_get_attributes(item):
    """Проверка получения атрибутов экземпляра класса Item"""
    assert item.name == 'товар 1'
    assert item.price == 10000
    assert item.quantity == 20
    assert item.pay_rate == 0.85
    assert len(Item.all) == 1


def test_change_attributes(item):
    """Проверка изменения атрибутов"""
    item.name = 'товар 1_'
    item.price = 10
    item.quantity = 10
    item.pay_rate = 0.5

    assert item.name == 'товар 1_'
    assert item.price == 10
    assert item.quantity == 10
    assert item.pay_rate == 0.5


def test_calculate_total_price(item):
    """Проверка расчета общей стоимости товаров"""
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    """Проверка применения скидки на товар"""
    item.pay_rate = 0.8
    assert item.apply_discount() == 8000
    assert item.price == 8000


def test_object_name_str(item):
    """Проверка отображения информации об объекте класса Item для пользователей"""
    assert str(item) == 'товар 1'


def test_object_name_repr(item):
    """Проверка отображения информации об объекте класса Item для разработчиков"""
    assert repr(item) == 'Item(name=товар 1, price=10000, quantity=20)'


def test_exception_long_name(item):
    """Проверка вызова исключения, если название товара будет превышать 10 символов"""
    with pytest.raises(Exception):
        item.name = 'длина названия товара больше 10 символов'


def test_instantiate_from_csv():
    """
    Проверка атрибутов экземпляров, созданных из файла csv.
    Проверка, что создано правильное количество экземпляров.
    """
    Item.instantiate_from_csv(path=os.path.join('tests', 'test.csv'))
    item_1 = Item.all[0]
    item_2 = Item.all[1]
    item_3 = Item.all[2]

    assert len(Item.all) == 3
    assert item_1.name == 'товар 1'
    assert item_1.price == 100
    assert item_1.quantity == 1
    assert item_2.name == 'товар 2'
    assert item_2.price == 55.5
    assert item_2.quantity == 3
    assert item_3.name == 'товар 3'
    assert item_3.price == 2000
    assert item_3.quantity == 6


def test_attributes_price_and_quantity():
    """
    Проверка того, что при инициализации объекта класса Item
    нельзя задать атрибуты цена и количество меньше 0
    """
    with pytest.raises(AttributeError):
        Item(name='товар 1', price=-10000, quantity=-1)


def test_add(item):
    """
    Проверка сложения двух экземпляров класса Item.
    Сложение происходит по атрибуту quantity.
    """
    assert item + item == 40


def test_add_exception(item):
    """
    Проверка вызова исключения, если правый операнд не является
    экземпляром класса Item
    """
    with pytest.raises(TypeError):
        result = item + 10
