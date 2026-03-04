class Calculator:
    def __init__(self, a, b, wynik = 0):
        self.a = a
        self.b = b
        self.wynik = wynik

    def add(self):
        self.wynik = self.a + self.b
        return self.wynik

    def subtract(self):
        self.wynik = self.a - self.b
        return self.wynik

    def multiply(self):
        self.wynik = self.a * self.b
        return self.wynik

    def divide(self):
        if self.b == 0:
            raise ValueError("Nie można dzielić przez 0")
        self.wynik = self.a / self.b
        return self.wynik

calculator = Calculator(10, 0)
calculator.divide()