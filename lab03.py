from math import sin, cos
print(" 1 - Вычислить функцию G\n "
      " 2 - Вычислить функцию F\n "
      " 3 - Вычислить функцию Y\n "
      " 0 - Выход из программы \n ")
num1 = float(input('Значение\n'))
if num1 == 0:
    print("До свидания!")
else:
    a = float(input("Введите а: "))
    x_min = float(input("Введите минимальное значение x: "))
    x_max = float(input("Введите макимальное значение х: "))
    step_c = int(input("Введите число шагов: "))
    step = int
    step = (x_max - x_min) / (step_c - 1)

    if num1 == 1:
        while x_min <= x_max:
            T = (-10 * a ** 2 + 11 * a * x_min + 3 * x_min ** 2)
            if T > 0.000000001:
                G = 5 * (-2 * a ** 2 + a * x_min + 3 * x_min ** 2) / T
                print('a = {}, x = {}, Result: {}'.format(a, x_min, G))
            else:
                print('Vvedite drugoe znachenie')
            x_min += step
    elif num1 == 2:
        while x_min <= x_max:
            F = sin(10 * a ** 2 - 7 * a * x_min + x_min ** 2)
            print('a = {}, x = {}, Result: {}'.format(a, x_min, F))
            x_min += step
    elif num1 == 3:
        while x_min <= x_max:
            Y = sin(1) / cos(45 * a ** 2 - 79 * a * x_min + 30 * x_min ** 2)
            print('a = {}, x = {}, Result: {}'.format(a, x_min, Y))
x_min += step