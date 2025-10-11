import math

def f(x):
    """Исходная функция: f(x) = x * 2^x - 1"""
    return x * (2 ** x) - 1


def df(x):
    """Производная функции: f'(x) = 2^x * (1 + x * ln(2))"""
    return (2 ** x) * (1 + x * math.log(2))


def newton_method(x0, eps=0.01, nmax=100):
    """
    Метод Ньютона для решения уравнения f(x)=0
    """
    print("Метод Ньютона для уравнения x*2^x - 1 = 0")
    print(f"Начальное приближение: x0 = {x0}")
    print(f"Точность: ε = {eps}")
    print(f"Максимальное число итераций: {nmax}")
    print("=" * 70)

    xn = x0
    print("{:<3} {:<12} {:<15} {:<15} {:<12} {:<12}".format(
        'n', 'x_n', 'f(x_n)', "f'(x_n)", 'x_n+1', 'eps'))
    print("-" * 70)

    for n in range(1, nmax + 1):
        f_xn = f(xn)
        df_xn = df(xn)

        if abs(df_xn) < 1e-12:
            print(f"Ошибка: производная близка к нулю в точке x_{n} = {xn}")
            return None

        xn1 = xn - f_xn / df_xn
        error = abs(xn1 - xn)

        print("{:<3} {:<12.6f} {:<15.6e} {:<15.6e} {:<12.6f} {:<12.6e}".format(
            n, xn, f_xn, df_xn, xn1, error))

        if error < eps:
            print("=" * 70)
            print(f"Корень найден: x = {xn1:.6f}")
            print(f"Количество итераций: {n}")
            print(f"Точность: {error:.2e}")
            return xn1

        xn = xn1

    print("=" * 70)
    print(f"Достигнуто максимальное количество итераций ({nmax})")
    print(f"Текущее приближение: x = {xn:.6f}")
    return xn


def test_cases():
    """Тестовые случаи"""
    print("ТЕСТИРОВАНИЕ МЕТОДА НЬЮТОНА")
    print("=" * 70)

    # Тест 1
    print("\nТест 1: Основной случай")
    newton_method(x0=0.5, eps=0.01, nmax=10)

    # Тест 2
    print("\nТест 2: Большая точность")
    newton_method(x0=1.0, eps=0.001, nmax=10)

    # Тест 3
    print("\nТест 3: Другое начальное приближение")
    newton_method(x0=0.0, eps=0.01, nmax=10)

    # Тест 4
    print("\nТест 4: Ограничение итераций")
    newton_method(x0=0.5, eps=0.0001, nmax=3)

    # Тест 5
    print("\nТест 5: Проверка особых случаев")
    newton_method(x0=0.0, eps=0.01, nmax=10)


# Основная программа
if __name__ == "__main__":
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Метод Ньютона для решения уравнения x*2^x - 1 = 0")
    print("=" * 70)

    result = newton_method(x0=0.5, eps=0.01, nmax=10)

    print("\n" + "=" * 70)
    test_cases()
