import numpy as np

def main():
    # Матрица коэффициентов A
    A = np.array([
        [2, 3, -1],
        [1, -2, 1],
        [1, 0, 2]
    ], dtype=float)

    # Вектор свободных членов b
    b = np.array([9, 3, 2], dtype=float)

    # Проверка детерминанта
    det = np.linalg.det(A)

    if det == 0:
        print("Система вырожденная, решения нет или их бесконечно много.")
    else:
        # Решение через обратную матрицу
        A_inv = np.linalg.inv(A)
        x = A_inv @ b

        # Красивый вывод
        print("Решение системы:")
        print(f"x = {x[0]:.2f}")
        print(f"y = {x[1]:.2f}")
        print(f"z = {x[2]:.2f}")

if __name__ == "__main__":
    main()
