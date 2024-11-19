# Необходимо реализовать декоратор `@strict`
# Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов, объявленным в
# прототипе функции. (подсказка: аннотации типов аргументов можно получить из атрибута объекта функции
# `func.__annotations__` или с помощью модуля `inspect`). При несоответствии типов бросать исключение `TypeError`
# Гарантируется, что параметры в декорируемых функциях будут следующих типов: `bool`, `int`, `float`, `str`
# Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию
#
#
# ```python3
# def strict(func):
#     ...
#
#
# @strict
# def sum_two(a: int, b: int) -> int:
#     return a + b
#
#
# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
# ```

MyType = (bool, int, float, str)


def strict(func):
    def wrapper(*args):
        # anno = func.__annotations__
        # print(anno)
        # [print(f'{i} --> {type(i)}') for i in args]
        a, b = args
        if type(a) != type(b):
            raise TypeError(f'Типы параметров не должны различаться: {type(a)} != {type(b)}')
        return func(a, b)

    return wrapper


@strict
def sum_two(
        a: MyType,
        b: MyType
) -> MyType:
    return a + b


if __name__ == '__main__':
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(False, False))  # >>> 0
    print(sum_two(False, True))  # >>> 1
    print(sum_two('False', 'True'))  # >>> FalseTrue
    # print(sum_two(1, 2.4))  # >>> TypeError
