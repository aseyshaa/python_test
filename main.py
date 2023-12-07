import random
import string


def main_menu():
    print("Меню:")
    print("1. Ввести исходные данные вручную")
    print("2. Сгенерировать случайные исходные данные")
    print("3. Выполнить алгоритм")
    print("4. Вывести результат")
    print("5. Завершить работу")


def main():
    text = ""
    key = ""
    encrypted_text = ""
    while True:
        main_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            text, key = input_data_manually()
            encrypted_text = ""
        elif choice == "2":
            text, key = input_data_random()
            print("Выбранный текст - " + text)
            print("Выбранный ключ - " + key)
            encrypted_text = ""
        elif choice == "3":
            if text and key:
                encrypted_text = vigenere_cipher(text, key)
                print("Алгоритм выполнен.")
            else:
                print("Введите исходные данные перед выполнением алгоритма.")
        elif choice == "4":
            if encrypted_text:
                print("Зашифрованный текст: " + encrypted_text)
            else:
                print("Результаты алгоритма не получены.")
        elif choice == "5":
            break
        else:
            print("Неверный выбор пункта меню. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
