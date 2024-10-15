from src.category import Category, category1, category2
from src.product import Product


def test_category_init():
    category = Category("Test Category", "Test Description", [])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == ""


def test_category_count():
    category1 = Category("Category 1", "Description of category 1", [])
    category2 = Category("Category 2", "Description of category 2", [])
    assert Category.category_count == 0


def test_product_count():
    product1 = Product("Product 1", "Description 1", 99.99, 10)
    product2 = Product("Product 2", "Description 2", 199.99, 5)
    category = Category("Test Category", "Test Description", [])
    category.add_product(product1)
    category.add_product(product2)
    assert Category.product_count == 4


def test_category_products_property(first_category):
    assert first_category.products == 'Samsung, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n'


def test_add_product():
    product = Product('1', '2', 3.0, 4)
    product.name = '1'
    product.description = '2'
    product.__price = 180000.0
    product.quantity = 5


def test_products_property():
    category = Category("Test Category", "Test Description", [])
    product1 = Product("Product 1", "Test Description", 50, 5)
    product2 = Product("Product 2", "Test Description", 75, 3)
    category.add_product(product1)
    category.add_product(product2)
    expected_output = (
        "Product 1, 50 руб. Остаток: 5 шт.\n"
        "Product 2, 75 руб. Остаток: 3 шт.\n"
    )
    assert category.products == expected_output
