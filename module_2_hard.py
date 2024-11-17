first_number = int(input("Введите первое число от 3 до 20: "))
result = []
for i in range(1, first_number):
    for n in range(i, first_number):
        if (i+n == first_number or first_number % (i+n) == 0) and i != n:
            result.append(i)
            result.append(n)
print('Пароль: ', *result, sep='')
