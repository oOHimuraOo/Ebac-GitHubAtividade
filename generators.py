##iterator
# traditional way

x = [1,2,3,4,5]
for i in x :
    print(i)

#same thing, but different
x = [1,2,3,4,5]

y = iter(x)
try:
    while True:
        print(next(y))
except StopIteration as e:
    pass

# A simple generator function:
def my_gen():
    n = 1
    print(f'Primeiro print, n é igual a {n}')
    yield n

    n += 1
    print(f'segundo print, n é igual a {n}')
    yield n

    n += 1
    print(f'terceiro e ultimo print, n é igual a {n}')
    yield n

test = my_gen()
next(test)
next(test)
next(test)
next(test)