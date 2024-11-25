first = input('Введите first:')
second = input('Введите second:')
third= input('Введите third:')
if first == second == third:
    print (3, ' Совпадения')
elif first == second or second == third or first == third:
    print(2, ' Совпадения')
else:
    print(0, ' Совпадений')
