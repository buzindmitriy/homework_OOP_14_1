from src.product import product2, product1


class Category:
    """Класс для описания категории товара"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1

    def add_product(self, product):
        self.products.append(product)
        Category.product_count += 1


category1 = Category("Category 1", "Description of category 1", [])
category1.add_product(product1)
category1.add_product(product2)

category2 = Category("Category 2", "Description of category 2", [])
