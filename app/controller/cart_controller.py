from flask import Flask, jsonify, request
from app.domain.entities import Product
from app.repository.product_repository import ProductRepository
from app.usecases.cart_usecase import Cart

app = Flask(__name__)

product_repository = ProductRepository()  #se instancia la clase ProductRepository
cart_usecase = Cart(product_repository)   #se instancia la clase Cart

#Metodo para añadir un producto
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json  #se espera un JSON con la información del producto a agregar
    product_id = data.get('id')
    product_name = data.get('name')
    product_price = data.get('price')
    product = Product(product_id, product_name, product_price)
    try:
        cart_usecase.add_product_to_cart(product)
        return jsonify({"message": "El producto se adiciono correctamente"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


#Metodo para eliminar un producto
@app.route('/remove_product', methods=['POST'])
def remove_product():
    data = request.json #se espera un JSON con la información del producto a elimimnar
    product_id = data.get('id')
    try:
        cart_usecase.remove_product_from_cart(product_id)
        return jsonify({"message": "El producto se elimino correctamente"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


#Metodo para calcular el total de productos
@app.route('/calculate_total', methods=['GET'])
def calculate_total():
    total = cart_usecase.calculate_total()
    return jsonify({"total": f'El total de productos es: "{total}"'}), 200


if __name__ == '__main__':
    app.run(debug=True)
