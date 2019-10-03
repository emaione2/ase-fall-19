
def sum(m, n):
    increment = 1
    if n < 0:
        increment = -1
        n = abs(n)

    for i in range(n):
        m += increment
    return m


def get_sign(m, n):
    if (m < 0 and n > 0) or (m > 0 and n < 0):
        return -1
    else:
        return 1


def divide(m, n):
    if n == 0:
        raise ZeroDivisionError("EXCEPTION: divided by 0")
    sign = get_sign(m, n)
    d = 0
    m = abs(m)
    n = abs(n)
    m -= n
    while m >= 0:
        d += 1
        m -= n
    return d * sign


# print(sum(5, 3))

# print(divide(20, -2))

# r = range(6)

# print(r[5])

# try:
#     divide(100, 0)
# except:
#     print("ERROR!!!!")
