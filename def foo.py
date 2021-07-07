def foo(x):
    print('foo(', x, ') is called')

def bar(x, y):
    print(x + y)

import lib

lib.foo(5)
lib.bar(2,3)
