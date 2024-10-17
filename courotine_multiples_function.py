def func1():
    print('function 1 part 1')
    yield
    print('function 1 part 2')
    yield
    print('function 1 part 3')
    yield
    print('function 1 part 4')
    yield
    print('function 1 part 5')


def func2():
    print('function 2 part 1')
    yield
    print('function 2 part 2')
    yield
    print('function 2 part 3')
    yield
    print('function 2 part 4')
    yield
    print('function 2 part 5')

try:
    a = func1()
    b = func2()
    next(a)
    next(b)
    next(a)
    next(b)
    next(a)
    next(b)
    next(a)
    next(a)
    next(b)
    next(b)
    next(b)


except StopIteration as e:
    pass