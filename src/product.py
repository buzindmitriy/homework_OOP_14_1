class Product:
    """Класс для описания товара"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product):
        return cls(dict_product['name'], dict_product['description'], dict_product['price'], dict_product['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def prise(self, new_price: int):
        if new_price <= 0:
            raise ValueError("Price must be positive")
            self.__price = new_price
        self.__price = new_price


product1 = Product("Product 1", "Description 1", 99.99, 10)
product2 = Product("Product 2", "Description 2", 199.99, 5)
