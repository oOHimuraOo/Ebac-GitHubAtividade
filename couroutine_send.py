def func():
    print('Function part 1')

    x = yield
    print(x)
    print('function part 2')

    a = yield
    print(a)
    print('function part 3')


try:
    y = func()
    next(y)
    y.send(6)
    y.send(12)

except StopIteration as e:
    pass