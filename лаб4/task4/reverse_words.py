import re

def reverse_words():
    text = input("Введите строку: ")
    new_text = re.sub(r'^\w+|\w+$', lambda m: m.group(0)[::-1], text)
    print("Результат:", new_text)
