try:
    def avg_test_case() -> int:
        total_quantity_test_case = 0
        for i in range(7):
            total_quantity_test_case += int(input("Ведите количество пройденный тест-кейсов: "))
        return total_quantity_test_case // 7
    avg_quantity_test_case = avg_test_case()
    if avg_quantity_test_case >= 10:
        print(f"Средние количество тест-кейсов {avg_test_case()}\nСтремись только вперед!")
    else:
        print("Попробуйте улучшить результат.")
except ValueError:
    print("Введите число")
