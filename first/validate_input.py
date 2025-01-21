while True:
    age = input("Введите ваш возраст: ")
    if not age.isdigit():
        print("Это не число. Введите снова.")
    else:
        age = int(age)
        if 0 <= age <= 120:
            print("Возраст принят!")
            break
        else:
            print("Некорректный возраст. Попробуйте снова.")

while True:
    user_name = input("Введите ваше имя: ")
    if not user_name.isalpha() or not user_name[0].isupper():
        print("Некорректное имя. Попробуйте снова.")
    else:
        print(user_name)
        break
