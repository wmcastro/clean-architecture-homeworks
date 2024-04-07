class Calculadora:
    
    def sumar(self, x, y):
        z= x + y
        return z

    def restar(self, x, y):
        z= x - y
        return z

    def multiplicar(self, x, y):
        z= x * y
        return z

    def dividir(self, x, y):
        if y != 0:
            z= x / y
            return z
        else:
            return "Error: división por cero"

