def validate(user_):
    if not isinstance(user_, str):
        return "Ошибка: данные должно быть строкой."

    if not (3 <= len(user_) <= 20):
        return "Ошибка: данные должно содержать от 3 до 20 символов."

    if not user_.isalpha():
        return "Ошибка: данные должно содержать только буквы."

    return "Данные приняты успешно."


username = input("Введите имя пользователя: ")
print(validate(username))
user_prof = input(f"{username} какая у вас проффесия: ")
print(validate(user_prof))
user_age = input(f"Сколько лет {username} работает в QA?: ")
if not user_age.isdigit():
    print("Ошибка: данные должны содержать только цифры.")
user_knows = input(f"Что такое переменная? да / нет: ")
if user_knows == 'да':
    print("Молодец!")
else:
    print("Переменные в Python — это именованные ссылки на объекты, которые хранятся в памяти компьютера")
