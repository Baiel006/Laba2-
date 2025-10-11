def first_task():
    x = int(input("Введите число от 1 до 9: "))

    if 1 <= x <= 3:
        s = input("Введите строку: ")
        n = int(input("Введите число повторов: "))
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
