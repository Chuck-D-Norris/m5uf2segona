class Calculadora:
    def __init__(self):
        """Constructor de la classe. Inicialitza la calculadora."""
        print("Calculadora inicialitzada.")

    def sumar(self, a, b):
        """Retorna la suma de dos nombres."""
        return a + b

    def restar(self, a, b):
        """Retorna la resta de dos nombres."""
        return a - b

    def multiplicar(self, a, b):
        """Retorna el producte de dos nombres."""
        return a * b

    def dividir(self, a, b):
        """Retorna la divisió de dos nombres. Si el divisor és 0, llença un error."""
        if b == 0:
            raise ValueError("No es pot dividir per zero.")
        return a / b

    def factorial(self, n):
        """Retorna el factorial d'un nombre enter no negatiu. Si el nombre és negatiu, llença un error."""
        if n < 0:
            raise ValueError("El factorial no està definit per nombres negatius.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Exemple d'ús de la classe Calculadora
calc = Calculadora()
print("Suma: ", calc.sumar(5, 3))
print("Resta: ", calc.restar(5, 3))
print("Multiplicació: ", calc.multiplicar(5, 3))
print("Divisió: ", calc.dividir(5, 3))
print("Factorial: ", calc.factorial(5))
