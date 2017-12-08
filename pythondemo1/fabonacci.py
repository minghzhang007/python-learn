def fab(n):
    a, b, i = 0, 1, 0
    while i < n:
        print(b, end=' ')
        a, b = b, a + b
        i += 1
    print()


def fab1(n):
    a, b = 0, 1
    result = []
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
    print()
