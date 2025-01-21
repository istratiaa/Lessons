string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")




if sorted(string1) == sorted(string2):
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")
