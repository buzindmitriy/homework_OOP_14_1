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
        self.price = price
        self.quantity = quantity


product1 = Product("Product 1", "Description 1", 99.99, 10)
product2 = Product("Product 2", "Description 2", 199.99, 5)
