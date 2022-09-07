import datetime


def logger_1(some_function): #задание 1
    def new_function(*args):
        result = some_function(*args)
        with open('logs/LOG.txt', "a", encoding='utf-8') as f:
            f.write(
                f'Время и дата вызова функции {datetime.datetime.now()}\nВызвана функция {some_function.__name__}\nВходные аргументы {args}\nФункция вернула {result}\n_________________________\n')
        f.close()
        return result
    return new_function



def logger_2(path): #задание 2
    def _logger(some_function):
        def new_function(*args):
            result = some_function(*args)
            with open(path, "a", encoding='utf-8') as f:
                f.write(f'Время и дата вызова функции {datetime.datetime.now()}\nВызвана функция {some_function.__name__}\nВходные аргументы {args}\nФункция вернула {result}\n_________________________\n')
            f.close()
            return result
        return new_function
    return _logger




