# 2020 Практика программирования Python Lesson 7
# New commit in github at 22.52 10.06.2021
# Модули и пакеты
# import
import math
from builtins import function

import module as module

math.sin(math.pi)
# Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
# runfile('C:/Users/vlad/PycharmProjects/git_learning/Lesson 7.py', wdir='C:/Users/vlad/PycharmProjects/git_learning')
import math
import cmath
math.sin(math.pi)
var = 1.2246467991473532e-16
cmath.sin(math.pi)
(1.2246467991473532e-16-0j)
x = 1 + 1j
# math.sin(x)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: can't convert complex to float
cmath.sin(x)
(1.2984575814159773+0.634963914784736j)
from cmath import *
help(sin)


class Help:
    pass


Help on built-in function sin in module cmath:


def z(args):
    pass


sin(z, /)
    Return the sine of z.
from cmath import *
help(sin)
Help on built-in function sin in module cmath:
sin(z, /)
    Return the sine of z.
sin(1) # sinus 1 - вещественное число
(0.8414709848078965+0j) # даёт комплексное число
from math import *
sin(1) # sinus 1 - вещественное число
0.8414709848078965 # - даёт вещественное число
help(sin)
Help on built-in function sin in module math:
sin(x, /)
    Return the sine of x (measured in radians). # возвращает синус х измеренный в радианах
import cmath as cm
import math as m
cm.sin(1)
(0.8414709848078965+0j)
m.sin(1)
0.8414709848078965
# stop at 47 minute & go to sleep
def foo(x):
    print('foo(', x, ') is called')

def bar(x, y):
    print(x + y)

# Объекты и классы
"""Объект - это переменная классового типа"""
"""значение - тип (родовое понятие)"""
"""объект - класс (видовое понятие)"""
"""Создаём class Goat:"""
"""pass"""
"""Этот маленький код создаёт новый класс"""
"""Экземпляр класса - это тот же самый объект"""
"""mashka = Goat() - конструирование (создание) нового объекта, класса"""
"""РЕР8 - имена классов должны начинаться с большой буквы"""
"""Класс - это коробочка для упаковывания ф-ций и переменных"""
"""Модуль как и класс - это объединение данных и програмного кода, который эти данные обрабатывает"""
"""Класс - это объединение (инкапсуляция) кода и данных"""
#class Goat:
#    age = 0 - классовое свойство (атрибут)
#    def pet():
#        print("Hello")
"""Ещё один класс:"""
#class Cow:  и т д
"""Внутри класса есть переменные и функции"""
"""Можно создать двух разных коз"""
# a = Goat()
# b = Goat()
#a.pet()
#b.pet()
# a.age = 5 - экземплярное свойство
# b.name = "Mashka"
""" В классах делают конструктор, который занимается конструированием, 
эта функция называется: def __init__(set f...) """
"""Отличие в том, что мы не можем создавать экземпляры модуля, 
потому что у модуля нет конструктора"""
"""Модуль - это более древний механизм, он предполагает разбиение на подпапки, 
в которых могут находиться и функции и классы"""
"""На этом урок закончился"""
