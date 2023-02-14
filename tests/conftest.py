import pytest
from shop.shop import Item

@pytest.fixture
def item():
    return Item(name='тестовый товар', price=10000, quantity=20)
