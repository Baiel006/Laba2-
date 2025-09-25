# --- Задание 1: Первое задание с генератором списков ---
def first_task():
    x = int(input("Введите число от 1 до 9: "))

    if 1 <= x <= 3:
        s = input("Введите строку: ")
        n = int(input("Введите число повторов: "))
        # Генератор списков для повторения строки n раз
        print(*(s for _ in range(n)), sep="\n")

    elif 4 <= x <= 6:
        m = int(input("Введите степень, в которую возвести число: "))
        print(f"Результат возведения числа {x} в степень {m} равен: {x ** m}")

    elif 7 <= x <= 9:
        for _ in range(10):
            x += 1
            print(x)
    else:
        print("Ошибка ввода")


# --- Задание 2: Общество в XXI веке с функцией ---
def second_task():
    print("Общество в начале XXI века")
    age = int(input("Введите ваш возраст: "))
    if 0 <= age < 7:
        print("Вам в детский сад")
    elif 7 <= age < 18:
        print("Вам в школу")
    elif 18 <= age < 25:
        print("Вам в профессиональное учебное заведение")
    elif 25 <= age < 60:
        print("Вам на работу")
    elif 60 <= age <= 120:
        print("Вам предоставляется выбор")
    else:
        # Пятикратный вывод ошибки
        for _ in range(5):
            print("Ошибка! Это программа для людей!")


# --- Задание 3: Вывод слов и их длины ---
def print_words_with_length():
    text = input("Введите строку: ")
    for word in text.split():
        print(f"{word} - {len(word)}")


# --- Задание 4: Цепное возведение в степени ---
def chain_powers(*args):
    if not args:
        return []
    result = [args[0] ** 1]  # Первое число в степень 1
    for prev, current in zip(args, args[1:]):
        result.append(current ** prev)
    return result



def main():
    while True:
        print("\nВыберите задание:")
        print("1 - Первое задание")
        print("2 - Задание Общество")
        print("3 - Вывод слов и их длины")
        print("4 - Цепное возведение в степени")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            first_task()
        elif choice == "2":
            second_task()
        elif choice == "3":
            print_words_with_length()
        elif choice == "4":
            nums = input("Введите числа через пробел: ").split()
            nums = [int(n) for n in nums]
            print("Результат:", chain_powers(*nums))
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Нет такого задания.")

        # Спрашиваем пользователя, хочет ли он продолжить
        cont = input("\nХотите выполнить ещё одно задание? (да/нет): ").strip().lower()
        if cont != "да":
            print("Программа завершена.")
            break


if __name__ == "__main__":
    main()