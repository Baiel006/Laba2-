import os
import csv
import json
import re
from datetime import datetime


def get_unique_filename(folder, base_name, ext):
    """Создаёт уникальное имя файла с текущей датой и временем в указанной папке"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(folder, f"{base_name}_{timestamp}{ext}")


# ---------------- ЗАДАНИЕ 1: Подсчёт из TXT ----------------
def task1_txt():
    """
    Считывает TXT файл с товарами.
    В строке указывается один товар с количеством штук или пар.
    Считает общее количество товаров в штуках и парах и сохраняет в конец файла.
    """
    file_path = input("Введите путь к TXT файлу: ").strip()
    if not os.path.exists(file_path):
        print("Файл не существует!")
        return

    folder = os.path.dirname(file_path)
    count_shtuki = 0
    count_pary = 0

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            line_lower = line.strip().lower()
            match_shtuki = re.search(r'(\d+)\s*(шт\.?|штук[аи]?)\b', line_lower)
            if match_shtuki:
                count_shtuki += int(match_shtuki.group(1))
            match_pary = re.search(r'(\d+)\s*(пар[аы]?)\b', line_lower)
            if match_pary:
                count_pary += int(match_pary.group(1))

        out_name = get_unique_filename(folder, "результат_txt", ".txt")
        with open(out_name, "w", encoding="utf-8") as f:
            f.writelines(lines)
            f.write(f"\nИтого товаров в штуках: {count_shtuki}\n")
            f.write(f"Итого товаров в парах: {count_pary}\n")

        print(f"Результат сохранён в: {out_name}")
        print(f"Итого штук: {count_shtuki}, пар: {count_pary}")

    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")


# ---------------- ЗАДАНИЕ 2: Подсчёт из CSV ----------------
def task2_csv():
    """
    Считывает CSV файл с товарами.
    Подсчитывает общее количество товаров в штуках и парах.
    Сохраняет результат в новый CSV файл.
    """
    file_path = input("Введите путь к CSV файлу: ").strip()
    if not os.path.exists(file_path):
        print("Файл не существует!")
        return

    folder = os.path.dirname(file_path)
    count_shtuki = 0
    count_pary = 0

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            rows = list(reader)

        for row in rows:
            for value in row.values():
                if value:
                    value_lower = str(value).strip().lower()
                    match_shtuki = re.search(r'(\d+)\s*(шт\.?|штук[аи]?)\b', value_lower)
                    if match_shtuki:
                        count_shtuki += int(match_shtuki.group(1))
                    match_pary = re.search(r'(\d+)\s*(пар[аы]?)\b', value_lower)
                    if match_pary:
                        count_pary += int(match_pary.group(1))

        out_name = get_unique_filename(folder, "результат_csv", ".csv")
        with open(out_name, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            writer.writerow({fieldnames[0]: "Итого товаров в штуках", fieldnames[1]: count_shtuki})
            writer.writerow({fieldnames[0]: "Итого товаров в парах", fieldnames[1]: count_pary})

        print(f"Результат сохранён в: {out_name}")
        print(f"Итого штук: {count_shtuki}, пар: {count_pary}")

    except Exception as e:
        print(f"Ошибка при обработке CSV файла: {e}")


# ---------------- ЗАДАНИЕ 3: Подсчёт из JSON ----------------
def task3_json():
    """
    Считывает JSON файл с товарами.
    Подсчитывает общее количество товаров в штуках и парах.
    Сохраняет результат в отдельный JSON файл.
    """
    file_path = input("Введите путь к JSON файлу: ").strip()
    if not os.path.exists(file_path):
        print("Файл не существует!")
        return

    folder = os.path.dirname(file_path)
    count_shtuki = 0
    count_pary = 0

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            if isinstance(item, dict):
                for value in item.values():
                    if value:
                        value_lower = str(value).strip().lower()
                        match_shtuki = re.search(r'(\d+)\s*(шт\.?|штук[аи]?)\b', value_lower)
                        if match_shtuki:
                            count_shtuki += int(match_shtuki.group(1))
                        match_pary = re.search(r'(\d+)\s*(пар[аы]?)\b', value_lower)
                        if match_pary:
                            count_pary += int(match_pary.group(1))

        out_name = get_unique_filename(folder, "результат_json", ".json")
        result = {"Итого товаров в штуках": count_shtuki, "Итого товаров в парах": count_pary}

        with open(out_name, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        print(f"Результат сохранён в: {out_name}")
        print(f"Итого штук: {count_shtuki}, пар: {count_pary}")

    except Exception as e:
        print(f"Ошибка при обработке JSON файла: {e}")


# ---------------- ЗАДАНИЕ 4: Структура папки ----------------
def task4_folder():
    """
    Сохраняет структуру указанной папки в JSON файл.
    В структуре отображаются подпапки и файлы.
    """
    folder_path = input("Введите путь к папке: ").strip()
    if not os.path.exists(folder_path):
        print("Папка не существует!")
        return

    def get_folder_structure(path):
        structure = {}
        for root, dirs, files in os.walk(path):
            rel_path = os.path.relpath(root, path)
            if rel_path == ".":
                rel_path = ""
            structure[rel_path] = {"dirs": dirs, "files": files}
        return structure

    structure = get_folder_structure(folder_path)
    out_name = get_unique_filename(folder_path, "структура_папки", ".json")
    with open(out_name, "w", encoding="utf-8") as f:
        json.dump(structure, f, ensure_ascii=False, indent=4)

    print(f"Структура папки сохранена в: {out_name}")


# ---------------- MAIN ----------------
def main():
    while True:
        print("\nВыберите задание:")
        print("1 - Подсчёт из TXT")
        print("2 - Подсчёт из CSV")
        print("3 - Подсчёт из JSON")
        print("4 - Сохранить структуру папки в JSON")
        print("0 - Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            task1_txt()
        elif choice == "2":
            task2_csv()
        elif choice == "3":
            task3_json()
        elif choice == "4":
            task4_folder()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()