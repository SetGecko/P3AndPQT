try:
    s = input("Введите данные: ")
    print(s)
except EOFError:
    print("Обработка исключения EOFError")
