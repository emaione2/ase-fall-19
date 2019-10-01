from Lecture1 import calculator as funcs


#from calculator import sum,divide

class calculator:
    def __init__(self):
        pass

    def sum(self, m, n):
        return funcs.sum(m, n)

    def div(self, m, n):
        return funcs.divide(m,n)


aCalculator = calculator()

print(aCalculator.sum(5, 3))
print(aCalculator.div(-30, 3))
