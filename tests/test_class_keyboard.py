import pytest

from shop.shop import Item


def test_get_attributes(keyboard):
    """Проверка получения атрибутов экземпляра класса Keyboard"""
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'
    assert keyboard.pay_rate == 0.85
    assert len(Item.all) == 1


def test_change_language_attribute(keyboard):
    """
    Проверка вызова исключения при попытке изменить атрибут language
    """
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'


def test_change_lang(keyboard):
    """
    Проверка метода изменения языка клавиатуры
    """
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'


def test_object_name_repr(keyboard):
    """Проверка отображения информации об объекте класса Keyboard для разработчиков"""
    assert repr(keyboard) == 'KeyBoard(name=Dark Project KD87A, price=9600, quantity=5)'
