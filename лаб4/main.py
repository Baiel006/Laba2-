from task1 import case_1_to_3, case_4_to_6, case_7_to_9, case_invalid
from task2.file_info import file_info
from task3.magic_ball import magic_ball
from task4.reverse_words import reverse_words


def main():
    while True:
        print("\nВыберите задание:")
        print("1 - Первое задание (пакет)")
        print("2 - Информация о файле/папке")
        print("3 - Шар предсказания")
        print("4 - Реверс слов в строке (регулярки)")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            x = int(input("Введите число от 1 до 9: "))
            if 1 <= x <= 3:
                case_1_to_3(x)
            elif 4 <= x <= 6:
                case_4_to_6(x)
            elif 7 <= x <= 9:
                case_7_to_9(x)
            else:
                case_invalid()

        elif choice == "2":
            file_info()
        elif choice == "3":
            magic_ball()
        elif choice == "4":
            reverse_words()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Нет такого задания.")


if __name__ == "__main__":
    main()
