def func():
    x = 5
    print(f'Function part 1, x = {x}')
    yield x

    x += 7
    print(f'Function part 3, x = {x}')

    yield  x

    print('function parte 3')


try:
    y = func()
    z = next(y)
    print(z)

    z = next(y)
    print(z)

    z = next(y)
    print(z)
except StopIteration as e:
    pass