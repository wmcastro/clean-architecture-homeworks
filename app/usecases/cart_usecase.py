class Cart:

    def __init__(self, product_repository):
    # está parte es para que cualquier instancia de esta clase tenda su propio atributo product_repository
    # con el valor que se recibe como segundo parametro de entrada
        self.product_repository = product_repository 

    # Función para agregar productos
    def add_product_to_cart(self, product):

        #valida que el precio no sea menor a cero
        if product.price < 0:
            raise ValueError("Ha fallado la adición del producto, el precio no puede ser negativo")

        #se da descuento del 10% si el producto vale más de 100  
        if product.price > 100:
            product.price = 0.9 * product.price 
        self.product_repository.add_product(product)

    def remove_product_from_cart(self, product_id):
        self.product_repository.remove_product(product_id)

    def calculate_total(self):
        total = 0
        for product in self.product_repository.get_all_products():
            total += product.price
        return total
