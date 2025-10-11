def print_words_with_length():
    text = input("Введите строку: ")
    for word in text.split():
        print(f"{word} - {len(word)}")
