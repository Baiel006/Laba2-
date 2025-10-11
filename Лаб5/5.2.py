class Society:
    def __init__(self, age):
        """Конструктор принимает возраст и вызывает нужный метод"""
        self.age = age
        self.route_by_age()  # Конструктор вызывает функцию класса в зависимости от атрибута

    def route_by_age(self):
        """Метод определяет, какой другой метод запустить"""
        print("\nОбщество в начале XXI века")

        if 0 <= self.age < 7:
            self.to_kindergarten()
        elif 7 <= self.age < 18:
            self.to_school()
        elif 18 <= self.age < 25:
            self.to_college()
        elif 25 <= self.age < 60:
            self.to_work()
        elif 60 <= self.age <= 120:
            self.to_choice()
        else:
            self.to_error()

    # --- Ниже все функции вынесены как методы класса ---
    def to_kindergarten(self):
        print("Вам в детский сад")

    def to_school(self):
        print("Вам в школу")

    def to_college(self):
        print("Вам в профессиональное учебное заведение")

    def to_work(self):
        print("Вам на работу")

    def to_choice(self):
        print("Вам предоставляется выбор")

    def to_error(self):
        for i in range(5):
            print("Ошибка! Это программа для людей!")


# --- Основная программа ---
while True:
    try:
        age = int(input("\nВведите ваш возраст: "))
        # Создание объекта вызывает конструктор, который сам выбирает метод
        person = Society(age)
    except ValueError:
        print("Ошибка ввода! Введите целое число.")
        continue

    choice = input("\nВведите 1 чтобы продолжить или 0 чтобы завершить: ")
    if choice == "0":
        print("Программа завершена.")
        break
