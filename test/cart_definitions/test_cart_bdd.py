import pytest
from pytest_bdd import given, scenario, then, when
from app.controller.cart_controller import app

# no sé si se necesita
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@scenario('test_cart.feature', 'Agregar producto al carrito con descuento del 10 porciento si su precio es mayor a 100')
def test_cart():
    pass

@given('un producto con precio <150>')
def producto_with_price(product_price):
    return product_price

@when('el producto se agrega al carrito')
def add_product(client, product_with_price):
    JSONproduct = {
    "id": "2",
    "name": "Ceviche de camaron",
    "price": "150"
    }
    return client.get(f'/add_product?valor={JSONproduct}')

@then('se otorga un descuento del 10%')
def se_otorga_descuento(add_product, product_with_price):
    product= add_product.data.decode('utf-8')
    if product.price== product_with_price()*0.9:
         prueba='exitosa'
    else :
         prueba= 'fallida'
    print(prueba)