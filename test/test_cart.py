import pytest
from app.domain.entities import Product
from app.repository.product_repository import ProductRepository
from app.usecases.cart_usecase import Cart



@pytest.fixture
def product_repository():
    return ProductRepository()

@pytest.fixture
def cart_usecase(product_repository):
    return Cart(product_repository)

def test_add_product_with_negative_price(cart_usecase):
    product = Product(id=1, name="Arroz con leche", price=-50)
    with pytest.raises(ValueError):
        cart_usecase.add_product_to_cart(product)


