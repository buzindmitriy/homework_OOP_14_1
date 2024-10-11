from src.product import Product

def test_product_init():
    product = Product("Test Product", "Test Description", 99.99, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 99.99
    assert product.quantity == 10


