from task1 import first_task
from task2 import second_task
from task3 import print_words_with_length
from task4 import chain_powers


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

        cont = input("\nХотите выполнить ещё одно задание? (да/нет): ").strip().lower()
        if cont != "да":
            print("Программа завершена.")
            break


if __name__ == "__main__":
    main()
