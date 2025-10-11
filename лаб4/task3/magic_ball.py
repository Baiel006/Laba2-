import random

def magic_ball():
    answers = [
        "Да", "Нет", "Возможно", "Скоро узнаешь",
        "Лучше не знать", "Конечно", "Никогда", "Сомнительно", "Точно"
    ]
    question = input("Задай свой вопрос: ")
    answer = random.choice(answers)
    print(f"{question} — {answer}")
