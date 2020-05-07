class Calculator:
    num = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addNumbers(self):
        return self.a + self.b


calc = Calculator(2, 3)
ans = calc.addNumbers()
print(ans)
