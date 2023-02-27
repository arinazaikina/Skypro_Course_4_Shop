import pytest

from shop.shop import Item, Phone


@pytest.fixture
def item():
    yield Item(name='товар 1', price=10000, quantity=20)
    Item.all.clear()


@pytest.fixture
def phone():
    yield Phone(name='iPhone 14', price=120000, quantity=5, number_of_sim=2)
    Item.all.clear()
