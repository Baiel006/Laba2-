import math

# Начальные приближения
x = 0.5
y = 0.5

# Точность
eps = 0.001
iteration = 0


while True:
    iteration += 1

    # Итерационные формулы (вариант A)
    x_new = (math.sin(y) - 1.6) / 2
    y_new = 0.8 - math.cos(x + 0.5)

    # Проверка сходимости
    if abs(x_new - x) < eps and abs(y_new - y) < eps:
        break

    # Обновление переменных
    x, y = x_new, y_new

# Результаты
print(f"Итерация: {iteration}")
print(f"x = {x_new:.6f}")
print(f"y = {y_new:.6f}")
