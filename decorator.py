def decorator(func_for_decor):
    def wraper(x, y):
        print('i will multiply next arguments: ', x, y)
        print('i have next result: ', func_for_decor(x, y))
        func_for_decor(x, y)
    return wraper


@decorator
def multiple(arg1, arg2):
    return arg1*arg2

multiple(3, 6)


# decorator without arguments
def my_decorator(function_for_decor):
    def wrapper():
        print('text1')
        function_for_decor()
        print('text2')
    return wrapper

@my_decorator
def func_1():
    print('between text')

func_1()

print(func_1.__doc__)
