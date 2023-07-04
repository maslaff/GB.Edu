try:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print(int(num1/num2))
except ValueError:
    print('Требуются числа')
except ZeroDivisionError:
    print('Деление на ноль недопустимо')


try:
    age = int(input('Введите ваш возраст: '))
    print(age)
except ValueError:
    print('Всё фигня, нужно число...')
