class InvalidNumberException(Exception):
    pass


class DivisionByZeroException(Exception):
    pass


def one():
    try:
        num = int(input('Введите число: '))
        if num <= 0:
            raise InvalidNumberException
        print(f'Вы ввели число {num}')
    except InvalidNumberException:
        print('Введите положительное число')


def two():
    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        if num1 == 0 or num2 == 0:
            raise DivisionByZeroException
        print(int(num1/num2))
    except ValueError:
        print('Требуются числа')
    except DivisionByZeroException:
        print('Деление на ноль недопустимо')


one()
# two()
