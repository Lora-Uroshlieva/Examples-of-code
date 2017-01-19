from functools import *


# Lesson 5. OOP

# 1. Написать функцию-обертку для другой функции (без явного объявления
#  декоратора, каррирование)

def multiplier(x):
    def f(y):
        print('Done. The result is: ', x * y)
        return x * y
    return f

mult_7 = multiplier(7)
print(mult_7(2))


# 2. Написать декоратор для функции, который будет возвращать
#  ссылку на оборачиваемую функцию

def wrapper(f):
    print('Done')
    return f

@wrapper
def f():
    return 1

print(f())
print(f)



# 3. Написать декоратор для функции без использования аргументов
def shaker(f):
    def wrapper():
        print('|------|')
        f()
        print('<\-----/>')

    return wrapper

def ice(f):
    def wrapper():
        print('..ice..')
        f()
    return wrapper

@shaker
@ice
def cocktail(fruit='.banana.'):
    print('..milk..')
    print(fruit)

cocktail()



# 4.Разработать декоратор для функции с поддержкой аргументов
# (без декоратора @wraps)
def decorator(x):
    def wrapper1(f):
        print('It\'s me, %s!' % x)
        def __(a):
            return f(a)
        return __
    return wrapper1


def make_hello(name):
    print('Hello, %s !' % name)

make_hello = decorator('Lora')(make_hello)('Misha')


# 5.Разработать декоратор для функции с поддержкой аргументов с использованием
#  функции wraps из стандартной библиотеки functools

def bar(func):
    @wraps(func)
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

print(foo.__name__)



# 6. Создать функцию и вызвать ее с помощью функции partial из стандартного
#  модуля functools. Создать и вызвать несколько функций с разным
#  кол-вом аргументов, где часть аргументов должна быть передана в partial,
# а остальная часть упущена для подальшей передаче их при вызове самой функции,
#  которая получена в результате вызова функции partial

# 7. Создать и проинициализировать класс
class Man:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
obj_1 = Man('Harry', 'Potter')
print(obj_1.firstname, obj_1.lastname)


# 8.Создать класс, который принимает некоторое кол-во аргументов и
#  устанавливает их, как новые его свойства
class Monitor:
    def __init__(self, price=0, producer='', diagonal=0):
        self.price = price
        self.model = producer
        self.diagonal = diagonal

samsung_mf_123 = Monitor(300, 'Samsung', 20)
print(samsung_mf_123.price)

# 9.Создать класс который содержит в себе public, protected и private свойства.
#  Написать вызов этих свойств, если свойство вызвать нельзя,
# то кратко написать почему



# 10. Создать 3 класса, где потом прописать цепочку наследования классов.
# Например A -> B -> C. Класс A является родителем для B, где B для С
class Tree:
    pass

class FruitTree(Tree):
    pass

class AppleTree(FruitTree):
    pass

#Tree -> FruitTree -> AppleTree

# 11. Создать класс A в котором определить конструктор, который должен
# принимать некое кол-во аргументов. Создать класс B, который наследуется от
#  класса A. В классе B переопределить конструктор из родительского класса,
# где написать вызов родительского конструктора с модификацией аргументов
# (например получаем аргумент а, где в родительский конструктор передаем a + 1)


# 12. Разработать класс с поддержкой оператора with."""
