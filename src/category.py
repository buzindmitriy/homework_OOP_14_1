from src.product import Product, product2, product1


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
        self.__products = products
        Category.product_count += len(self.products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def list_product(self):
        return self.__products


category1 = Category("Category 1", "Description of category 1", [])
category1.add_product(product1)
category1.add_product(product2)

category2 = Category("Category 2", "Description of category 2", [])
