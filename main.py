from product import Product
from product_manager import ProductManager
from cart import Cart


manager = ProductManager()
manager.add_product(Product("Laptop", 1500, 5))
manager.add_product(Product("Phone", 800, 10))

manager.display_products()
manager.calculate_total_value()
