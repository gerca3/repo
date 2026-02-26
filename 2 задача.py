number = int(input("Введите ограничение для совершенных чисел: "))
count = 1
while count <= number:
    flag = True
    for i in range(2, count):
        if count % i == 0:
            flag = False
            break
    if flag == True:
        print(count)
    count += 1