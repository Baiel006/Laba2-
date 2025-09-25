def task1():
    text = input("Введите строку: ")
    words = text.split()
    longest = max(words, key=len)
    print("Самое длинное слово:", longest, "| Количество букв:", len(longest))


def task2():
    text = input("Введите строку (слова через ;) : ")
    words = text.split(";")
    longest = max(words, key=len)
    print("Самое длинное слово:", longest, "| Количество букв:", len(longest))


def task3():
    text = input("Введите строку: ")
    delimiter = input("Введите символ-разделитель: ")
    words = text.split(delimiter)
    shortest = min(words, key=len)
    print("Самое короткое слово:", shortest, "| Количество букв:", len(shortest))


def task4():
    text = input("Введите строку: ")
    word = input("Введите слово для поиска: ")
    words = text.split()
    total = len(words)  # количество слов в строке

    if word in words:
        index = words.index(word) + 1  # +1 чтобы нумерация начиналась с 1
        print("Слово найдено:", word,
              "| Количество букв:", len(word),
              "| Позиция в строке:", index,
              "| Всего слов в строке:", total)
    else:
        print("Слово не найдено.",
              "| Всего слов в строке:", total)




def task5():
    text = input("Введите предложение: ")
    words = text.split()
    print("Количество слов:", len(words))
    # дополнительно выведем длину каждого слова
    for w in words:
        print(w, "-", len(w), "букв(ы)")


def main():
    while True:
        print("\nМеню:")
        print("1. Найти самое длинное слово (разделитель — пробел)")
        print("2. Найти самое длинное слово (разделитель — ; )")
        print("3. Найти самое короткое слово (разделитель задаёт пользователь)")
        print("4. Найти слово в строке")
        print("5. Посчитать количество слов (и длину каждого)")
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
