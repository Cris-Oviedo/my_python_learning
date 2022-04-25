

def add(a: int, b: int):
    try:
        print(a+b)
    except TypeError:
        print(f'Deben ser valores enteros: {a} + {b} no es posible ')


def rest(a: int, b: int):
    try:
        print(a - b)
    except TypeError:
        print(f'Deben ser valores enteros: {a} - {b} no es posible ')


if __name__ == '__main__':
    add(-1, 3)
    rest(4, 3)
