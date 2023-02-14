from shop.shop import Item


def test_get_attributes(item):
    assert item.name == 'тестовый товар'
    assert item.price == 10000
    assert item.quantity == 20
    assert item.pay_rate == 0.85
    assert len(Item.all) == 1

def test_set_attributes(item):
    item.name = 'товар 1'
    item.price = 1
    item.quantity = 1
    item.pay_rate = 0.5

    assert item.name == 'товар 1'
    assert item.price == 1
    assert item.quantity == 1
    assert item.pay_rate == 0.5

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000

def test_apply_discount(item):
    item.pay_rate = 0.8
    assert item.apply_discount() == 8000.0
    assert item.price == 8000.0

def test_object_name_str(item):
    assert str(item) == 'тестовый товар'

def test_object_name_repr(item):
    assert repr(item) == "'Item(тестовый товар, 10000, 20)'"
