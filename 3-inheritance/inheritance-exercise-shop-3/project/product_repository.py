from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for item in self.products:
            if item.name == product_name:
                return item

    def remove(self, product_name):
        item = self.find(product_name)
        if item is not None:
            self.products.remove(item)

    def __repr__(self):
        result = ''
        for item in self.products:
            result += f"{item.name}: {item.quantity}\n"
        return result.strip()



