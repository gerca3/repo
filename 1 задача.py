num = int(input("Введите число: "))
if (1 <= num <= 99) is False:
    raise ValueError("Ошибка! Число должно быть больше нуля и меньше ста")
k = int(input("Введите дополнительное число: "))
print(f"{k}{num}{k}")