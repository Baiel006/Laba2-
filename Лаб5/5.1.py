class Task1:
    def __init__(self, x):
        """Конструктор — принимает число x и запускает нужный метод"""
        self.x = x
        self.run_task()

    def run_task(self):
        """Определяет, какой метод запустить в зависимости от x"""
        if 1 <= self.x <= 3:
            self.repeat_string()
        elif 4 <= self.x <= 6:
            self.power_number()
        elif 7 <= self.x <= 9:
            self.increment_numbers()
        else:
            print("Ошибка ввода")

    def repeat_string(self):
        """Метод для повторения строки"""
        s = input("Введите строку: ")
        n = int(input("Введите количество повторов: "))
        for i in range(n):
            print(s)

    def power_number(self):
        """Метод для возведения числа в степень"""
        m = int(input("Введите степень: "))
        result = self.x ** m
        print("Результат:", result)

    def increment_numbers(self):
        """Метод для вывода последовательных чисел"""
        for i in range(10):
            self.x += 1
            print(self.x)


# --- Основная программа ---
while True:
    x = int(input("\nВведите число от 1 до 9: "))
    task = Task1(x)

    choice = input("\nВведите 1 чтобы продолжить или 0 чтобы завершить: ")
    if choice == "0":
        print("Программа завершена.")
        break
