
from figura.cuadrado import Cuadrado
from figura.rectangulo import Rectangulo

# Instancia un objeto cuadrado
cuadrado = Cuadrado(5)
print("Cuadrado:")
print("Área:", cuadrado.area())
print("Perímetro:", cuadrado.perimetro())

# Instancia un objeto rectángulo
rectangulo = Rectangulo(4, 6)
print("Rectángulo:")
print("Área:", rectangulo.area())
print("Perímetro:", rectangulo.perimetro())