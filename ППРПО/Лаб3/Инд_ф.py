import math

# Функция и её производная
def f(x):
    return x**2 - math.cos(x)

def df(x):
    return 2*x + math.sin(x)

# Метод простых итераций
def simple_iteration_method(x0, a, eps, nmax=100):
    print("МЕТОД ПРОСТЫХ ИТЕРАЦИЙ")
    print("Уравнение: x² - cos(x) = 0")
    print(f"Начальное приближение: x₀ = {x0}")
    print(f"Параметр релаксации: a = {a}")
    print(f"Точность ε = {eps}")
    print("=" * 75)
    print("n   xₙ           f(xₙ)        xₙ₊₁         |xₙ₊₁ - xₙ| ")
    print("-" * 75)

    def phi(x):
        return x - a * f(x)

    n = 0
    xn = x0
    while n < nmax:
        try:
            f_xn = f(xn)
            x_next = phi(xn)
            delta = abs(x_next - xn)

            print(f"{n+1:<3d} {xn:12.6f} {f_xn:12.6f} {x_next:12.6f} {delta:12.6f}")

            if delta < eps:
                print("=" * 75)
                print(f"✅ Корень найден: x = {x_next:.6f}")
                print(f"Количество итераций: {n+1}")
                print(f"Погрешность: {delta:.6e}")
                print(f"Значение функции: f(x) = {f(x_next):.6e}")
                print("=" * 75)
                return x_next

            xn = x_next
            n += 1

            # Защита от слишком больших значений
            if abs(xn) > 1e6:
                print("❌ Ошибка: значения вышли за допустимые пределы — расходимость.")
                return None

        except OverflowError:
            print("❌ Ошибка: переполнение при вычислениях (метод расходится).")
            return None

    print("=" * 75)
    print("❌ Превышено максимальное количество итераций.")
    return None


# ================== ТЕСТИРОВАНИЕ ==================
def test_cases():
    print("===========================")
    print("ТЕСТИРОВАНИЕ МЕТОДА ПРОСТЫХ ИТЕРАЦИЙ")
    print("===========================\n")

    print("ТЕСТ 1: Основной случай (x₀ = 0.5, a = 0.5, ε = 0.01)")
    simple_iteration_method(x0=-0.5, a=0.5, eps=0.01)
    print("\n")

    print("ТЕСТ 2: Повышенная точность (x₀ = 0.5, a = 0.5, ε = 0.001)")
    simple_iteration_method(x0=0.5, a=0.4, eps=0.001)
    print("\n")

    print("ТЕСТ 3: Другое начальное приближение и a (x₀ = 1, a = 0.4, ε = 0.01)")
    simple_iteration_method(x0=0.7, a=0.5, eps=0.01)
    print("\n")

    print("ТЕСТ 4: Ограничение итераций (x₀ = 1, a = 0.2, ε = 0.0001, nmax=5)")
    simple_iteration_method(x0=0.1, a=0.3, eps=0.0001, nmax=5)
    print("\n")

    print("ТЕСТ 5: Проверка особых случаев (x₀ = 0, a = 0.5, ε = 0.01)")
    simple_iteration_method(x0=0.0, a=0.5, eps=0.01)


# Запуск тестов
if __name__ == "__main__":
    test_cases()
