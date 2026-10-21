k = float(input("Введите размер кредита: "))
p = float(input("Введите годовой процент: "))
r = float(input("Введите прибыль за год: "))

if k <= 0 or p < 0 or r < 0:
    print("Ошибка: кредит должен быть положительным,",
          "процент и прибыль - неотрицательными")
else:
    debt = k
    savings = 0
    years = 0

    # Платежей до погашения нет, прибыль копится отдельно.
    while savings < debt:
        interest = debt * p / 100
        if r <= interest:
            break
        debt += interest
        savings += r
        years += 1

    if savings >= debt:
        print("Кредит можно погасить через", years, "лет")
        print("Накоплено:", round(savings, 2))
        print("Долг:", round(debt, 2))
    else:
        print("Накопить сумму для погашения кредита не получится")
