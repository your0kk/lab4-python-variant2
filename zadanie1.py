a = int(input("Введите A: "))
b = int(input("Введите B: "))

if a >= b:
    print("Ошибка: A должно быть меньше B")
else:
    count = 0
    print("Числа между A и B:")
    for number in range(b - 1, a, -1):
        print(number, end=" ")
        count += 1
    print("\nКоличество:", count)
