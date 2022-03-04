str = input("Введите имя пользователя")
print(len(str))
if len(str.split()) <= 0:
    print("Есть пробелы")
else:
    print("Пробелов нет")

a = int(input("Введите возраст пользователя"))
if a > 0 and a < 150:
    sum = 0
    proizv = 1
    while a > 0:
        b = a % 10
        sum = sum + b
        proizv = proizv * b
        a = a // 10
    print(sum)
    print(proizv)
else:
 print("Ошибка")
s = input('str:')
print(s.upper())
print(s.lower())
a = int(input("Введите возраст пользователя"))
if a > 0 and a < 150:
    print(a)
else:
    False

expression = input('Что вычислить?')
print(eval(expression))