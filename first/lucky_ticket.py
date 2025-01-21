ticket = input()

if len(ticket) != 6:
    print("Неверный номер билета")
if not ticket.isdigit():
    print("Билет должен состоять из цифр")
one_part_ticket = ticket[:3]
two_part_ticket = ticket[3:]


def summary(ticket: str) -> int:
    total_sum = 0
    for i in ticket:
        total_sum += int(i)
    return total_sum


if summary(one_part_ticket) == summary(two_part_ticket):
    print("Результат: билет счастливый.")
else:
    print("Результат: билет несчастливый.")