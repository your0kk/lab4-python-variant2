from math import log1p

x = float(input("Введите x (-1 <= x < 1): "))
eps = float(input("Введите точность (например, 0.001): "))

if not -1 <= x < 1 or eps <= 0:
    print("Ошибка: нужны -1 <= x < 1 и положительная точность")
else:
    total = 0
    n = 0
    term = -x
    error = abs(term)
    if x > 0:
        error = error / (1 - x)

    while error > eps and n < 1000000:
        total += term
        n += 1
        # Следующее слагаемое: -x ** (n + 1) / (n + 1)
        term = term * x * n / (n + 1)
        error = abs(term)
        if x > 0:
            error = error / (1 - x)

    print("Сумма ряда:", total)
    print("ln(1 - x):", log1p(-x))
    print("Разница:", abs(total - log1p(-x)))
    print("Количество слагаемых:", n)
    if error > eps:
        print("За 1000000 итераций заданная точность не достигнута")
