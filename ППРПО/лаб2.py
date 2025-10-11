import math
def f(x):
    """Исходная функция: x^2 - cos(x)"""
    return x ** 2 - math.cos(x)


def df(x):
    """Производная функции: 2x + sin(x)"""
    return 2 * x + math.sin(x)


def newton_method(x0, eps=0.01, nmax=100):
    """
    Метод Ньютона для решения уравнения f(x)=0

    Parameters:
    x0 - начальное приближение
    eps - точность
    nmax - максимальное число итераций

    Returns:
    корень уравнения или None в случае ошибки
    """
    print("Метод Ньютона для уравнения x^2 - cos(x) = 0")
    print(f"Начальное приближение: x0 = {x0}")
    print(f"Точность: ε = {eps}")
    print(f"Максимальное число итераций: {nmax}")
    print("=" * 60)

    xn = x0
    print(f"{'n':<3} {'x_n':<12} {'f(x_n)':<12} {'f\'(x_n)':<12} {'x_n+1':<12} {'eps':<12}")
    print("-" * 60)

    for n in range(1, nmax + 1):
        # Вычисляем значение функции и производной
        f_xn = f(xn)
        df_xn = df(xn)

        # Проверка на нулевую производную
        if abs(df_xn) < 1e-10:
            print(f"Ошибка: производная близка к нулю в точке x_{n} = {xn}")
            return None

        # Вычисляем следующее приближение
        xn1 = xn - f_xn / df_xn
        error = abs(xn1 - xn)

        # Вывод информации о текущей итерации
        print(f"{n:<3} {xn:<12.6f} {f_xn:<12.6f} {df_xn:<12.6f} {xn1:<12.6f} {error:<12.6f}")

        # Проверка условия остановки
        if error < eps:
            print("=" * 60)
            print(f"Корень найден: x = {xn1:.6f}")
            print(f"Количество итераций: {n}")
            print(f"Точность: {error:.2e}")
            return xn1

        xn = xn1

    print("=" * 60)
    print(f"Достигнуто максимальное количество итераций ({nmax})")
    print(f"Текущее приближение: x = {xn:.6f}")
    return xn


def test_cases():
    """Тестовые случаи"""
    print("ТЕСТИРОВАНИЕ МЕТОДА НЬЮТОНА")
    print("=" * 60)

    # Тест 1: Основной случай
    print("\nТЕСТ 1: Основной случай")
    print("x0 = -1, ε = 0.01, nmax = 10")
    result1 = newton_method(x0=-1, eps=0.01, nmax=10)

    # Тест 2: Большая точность
    print("\nТЕСТ 2: Большая точность")
    print("x0 = -1, ε = 0.001, nmax = 10")
    result2 = newton_method(x0=-1, eps=0.001, nmax=10)

    # Тест 3: Другое начальное приближение
    print("\nТЕСТ 3: Другое начальное приближение")
    print("x0 = -0.5, ε = 0.01, nmax = 10")
    result3 = newton_method(x0=-0.5, eps=0.01, nmax=10)

    # Тест 4: Ограничение итераций
    print("\nТЕСТ 4: Ограничение итераций")
    print("x0 = -1, ε = 0.0001, nmax = 3")
    result4 = newton_method(x0=-1, eps=0.0001, nmax=3)

    # Тест 5: Нулевая производная
    print("\nТЕСТ 5: Нулевая производная")
    print("x0 = 0, ε = 0.01, nmax = 10")
    result5 = newton_method(x0=0, eps=0.01, nmax=10)

    return result1, result2, result3, result4, result5


# Основная программа
if __name__ == "__main__":
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Метод Ньютона для решения уравнения x^2 - cos(x) = 0")
    print("=" * 60)

    # Основной расчет
    result = newton_method(x0=-1, eps=0.01, nmax=10)

    # Тестирование
    print("\n" + "=" * 60)
    test_cases()
