import math

# Ввод значений x и y с клавиатуры
x = float(input("Введите x:"))
y = float(input("Введите y:"))

# Вычисление значения выражения b
b = 0.1 * (x)**5 + ((math.e)**(-0.1*x)) - math.sqrt((math.fabs(x))*(math.fabs(x+y)))

# Вывод значений x, y и b
print("x:", x)
print("y:", y)
print("b:", b)
