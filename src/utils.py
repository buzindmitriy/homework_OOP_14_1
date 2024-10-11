import json
import os

from src.product import Product
from src.category import Category


def read_json(path):
    """Функция для чтения .json файлов"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Функция для создания объектов классов из .json файла"""
    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(**product_data)
            products.append(product)
        category = Category(**category_data)
        category.products = products
        categories.append(category)
    return categories


if __name__ == "__main__":
    product_list = read_json("../data/products.json")
    categories_data = create_objects_from_json(product_list)
    print(categories_data)
