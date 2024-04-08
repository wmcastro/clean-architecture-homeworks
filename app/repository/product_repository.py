class ProductRepository:
    def __init__(self):
        self.products = {}  # Inicializando products como un diccionario vacío

    def add_product(self, product):
        self.products[product.id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def get_all_products(self):
        return list(self.products.values())
