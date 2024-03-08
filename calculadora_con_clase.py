class Calculadora:
    def sumar(self, x, y):
        return x + y

    def restar(self, x, y):
        return x - y


calc = Calculadora()
print(calc.sumar(3, 4))
print(type(3))
print(type(calc))
print(type(Calculadora))
print(type(Calculadora.sumar))
