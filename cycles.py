# задача 1:
input_string = input("Введите строку: ")
index = 0
while index < len(input_string):
    print(input_string[index])
    index += 1

# задача 2:
correct_password = "secret"
attempts = 5
while attempts > 0:
    password = input("Введите пароль: ")
    if password == correct_password:
        print("Вы вошли в систему.")
        break
    else:
        attempts -= 1
        print(f"Неверный пароль. У вас осталось {attempts} попыток.")
else:
    print("Вы исключены из системы.")

# Задача 3:
price = float(input("Введите цену еды: "))
tip_percentage = float(input("Введите процент чаевых: "))
tip_amount = (tip_percentage / 100) * price
total_bill = price + tip_amount
print(f"Сумма чаевых: {tip_amount} рублей")
print(f"Общий счет: {total_bill} рублей")

# Задача 4:
numbers = [0, 0, 0, 1, 0, 1, 1]
found = False
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[i] = 1
        found = True
        break

if found:
    print("Первая ненулевая запись была изменена на 1:", numbers)
else:
    print("Нет ненулевых записей в списке.")