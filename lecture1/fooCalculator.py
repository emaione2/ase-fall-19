from lecture1 import calculator as funcs
# from calculator import sum,divide


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def sum(m, n):
        return funcs.sum(m, n)

    @staticmethod
    def div(m, n):
        return funcs.divide(m, n)


aCalculator = Calculator()

print(aCalculator.sum(5, 3))
print(aCalculator.div(-30, 3))
