def case_1_to_3(x: int):
    s = input("Введите строку: ")
    n = int(input("Введите число повторов: "))
    print(*(s for _ in range(n)), sep="\n")
