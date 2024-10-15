import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def first_product():
    return Product(
        name='Samsung',
        description='256GB, Серый цвет, 200MP камера',
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products=[
            Product('Samsung', '256GB, Серый цвет, 200MP камера', 180000.0, 5),
            Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
        ]
    )


@pytest.fixture
def product():
    return Product("Test Product", "Test Description", 100, 10)


# @pytest.fixture
# def category():
#     category = Category("Test Category")
#     category.add_product(Product("Product 1", "Description 1", 50, 5))
#     category.add_product(Product("Product 2", "Description 2", 75, 3))
#     return category


@pytest.fixture
def new_price():
    return -1000

# @pytest.fixture
# def product():
#     return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
