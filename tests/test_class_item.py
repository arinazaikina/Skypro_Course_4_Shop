import os

import pytest

from shop.shop import Item

def test_get_attributes(item):
    assert item.name == 'товар 1'
    assert item.price == 10000
    assert item.quantity == 20
    assert item.pay_rate == 0.85
    assert len(Item.all) == 1

def test_change_attributes(exist_item):
    exist_item.name = 'товар 1_'
    exist_item.price = 10
    exist_item.quantity = 10
    exist_item.pay_rate = 0.5

    assert exist_item.name == 'товар 1_'
    assert exist_item.price == 10
    assert exist_item.quantity == 10
    assert exist_item.pay_rate == 0.5

def test_calculate_total_price(exist_item):
    assert exist_item.calculate_total_price() == 100

def test_apply_discount(exist_item):
    exist_item.pay_rate = 0.8
    assert exist_item.apply_discount() == 8
    assert exist_item.price == 8

def test_object_name_str(exist_item):
    assert str(exist_item) == 'товар 1_'

def test_object_name_repr(exist_item):
    assert repr(exist_item) == "'Item(name=товар 1_, price=8.0, quantity=10)'"

def test_exception_long_name(exist_item):
    with pytest.raises(Exception):
        exist_item.name = 'длина названия товара больше 10 символов'

def test_instantiate_from_csv():
    Item.instantiate_from_csv(path=os.path.join('tests', 'test.csv'))
    item_2 = Item.all[1]
    item_3 = Item.all[2]
    item_4 = Item.all[3]

    assert len(Item.all) == 4
    assert item_2.name == 'товар 2'
    assert item_2.price == 100
    assert item_2.quantity == 1
    assert item_3.name == 'товар 3'
    assert item_3.price == 55.5
    assert item_3.quantity == 3
    assert item_4.name == 'товар 4'
    assert item_4.price == 2000
    assert item_4.quantity == 6
