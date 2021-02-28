#!

class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a/b

    def multiplication(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a * b

    def subtraction(self, a, b):
        return a - b
