def count_letters(word):
    return len(word)

word = "Hello, World!"
letter_count = count_letters(word)

# Запись результата в журнал
journal = {'task': 'Подсчет количества букв в слове', 'word': word, 'result': letter_count}
print(journal)