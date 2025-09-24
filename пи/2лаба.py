def task1():
    text = input("Введите строку: ")
    words = text.split()
    longest = max(words, key=len)
    print("Самое длинное слово:", longest)


def task2():
    text = input("Введите строку (слова через ;) : ")
    words = text.split(";")
    longest = max(words, key=len)
    print("Самое длинное слово:", longest)


def task3():
    text = input("Введите строку: ")
    delimiter = input("Введите символ-разделитель: ")
    words = text.split(delimiter)
    shortest = min(words, key=len)
    print("Самое короткое слово:", shortest)


def task4():
    text = input("Введите строку: ")
    word = input("Введите слово для поиска: ")
    if word in text.split():
        print("Слово найдено!")
    else:
        print("Слово не найдено.")


def task5():
    text = input("Введите предложение: ")
    words = text.split()
    print("Количество слов:", len(words))


def main():
    while True:
        print("\nМеню:")
        print("1. Найти самое длинное слово (разделитель — пробел)")
        print("2. Найти самое длинное слово (разделитель — ; )")
        print("3. Найти самое короткое слово (разделитель задаёт пользователь)")
        print("4. Найти слово в строке")
        print("5. Посчитать количество слов")
        print("0. Выход")

        choice = input("Выберите номер задания: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")


if __name__ == "__main__":
    main()
