class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_info()

    def calculate_total_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"Total inventory value: {total}")

    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]
