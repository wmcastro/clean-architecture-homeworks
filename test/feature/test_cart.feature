Feature: Add product to cart
    Scenario: Agregar producto al carrito con descuento del 10 porciento si su precio es mayor a 100
        Given un producto con precio
        When el producto se agrega al carrito
        Then se otorga un descuento del 10%