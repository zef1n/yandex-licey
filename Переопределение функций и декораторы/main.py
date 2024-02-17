# Дополнительные задачи
# Печать в верхнем регистре
# Определяем новую функцию print() с измененным поведением
def custom_print(func):
    def decorator(*args, **kwargs):
        args = [str(arg).upper() for arg in args]
        return func(*args, **kwargs)

    return decorator


print = custom_print(print)


# Пароль для Фибоначчи
def check_password(func):
    """ПАРОЛЬ - zef1n"""

    def decorator(*args, **kwargs):
        password = input("Введите пароль: ")
        if password == "zef1n":
            return func(*args, **kwargs)
        else:
            print("В доступе отказано")
            return None

    return decorator


@check_password
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Генератор декораторов

# Декоратор для кэширования
def cached(func):
    cache = dict()

    def decorator(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return decorator
