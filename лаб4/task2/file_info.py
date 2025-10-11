import os
import time

def file_info():
    folder = input("Введите путь к папке: ").strip()
    filename = input("Введите имя файла (или оставьте пустым, если хотите папку): ").strip()

    # если ввели файл — добавляем его к пути
    if filename:
        full_path = os.path.join(folder, filename)
    else:
        full_path = folder

    # заменим \ на /
    full_path = full_path.replace("\\", "/")

    if os.path.exists(full_path):
        obj_type = "директория" if os.path.isdir(full_path) else "файл"
        ctime = time.ctime(os.path.getctime(full_path))
        mtime = time.ctime(os.path.getmtime(full_path))

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
        else:
            size = sum(os.path.getsize(os.path.join(root, f))
                       for root, _, files in os.walk(full_path) for f in files)

        print(f"""
Полный путь: {full_path}
Размер: {size} байт
Тип объекта: {obj_type}
Дата создания: {ctime}
Дата изменения: {mtime}
""")
    else:
        print("Такого файла или папки нет.")

if __name__ == "__main__":
    file_info()
