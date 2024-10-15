from unittest.mock import patch, MagicMock

from src.product import Product
from src.category import Category


def test_product_init():
    product = Product("Test Product", "Test Description", 99.99, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 99.99
    assert product.quantity == 10


def test_price_update(capsys, first_product):
    first_product.__price = -100
    message = capsys.readouterr()
    assert message.out.strip() == ''


def test_new_product():
    product_dict = {
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 100,
        'quantity': 10
    }
    new_product = Product.new_product(product_dict)
    assert isinstance(new_product, Product)
    assert new_product.name == product_dict['name']
    assert new_product.price == product_dict['price']


def test_add_product():
    category = Category("Test Category", "Test Description", [])
    product = Product("Test Product", "Test Description", 100, 10)
    category.add_product(product)
    assert product in category._Category__products
    assert Category.product_count == 85
