a: int = 10
b: float = 1.23456
a = a + b
print(a)


def foo(c: int, d: str):
    c = d + str(c)
    print(c)


foo(a, 'ciao ')
