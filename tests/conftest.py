import pytest
from shop.shop import Item


@pytest.fixture
def item():
    return Item(name='товар 1', price=10000, quantity=20)


@pytest.fixture()
def exist_item():
    return Item.all[0]
