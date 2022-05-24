# Удалить из файла наименьшее нечетное число (см. замечание к предыдущей задаче).
'''
Алгоритм удаления: в компоненту, содержащую
максимальное число, скопировать последнюю компоненту файла,
а затем удалить последнюю компоненту с помощью truncate.
'''

'''
Работает при условии того, что каждое число записано с новой строки
и файл не содержит других символов, кроме чисел 0-9 и '-'
'''

file_name = 'testfile.txt'

file = open(file_name, 'r')

print('Читаем файл...')

line = file.readline()
print(line, end='')
x = int(line)

while line and x%2==0: #ищем первый нечётный номер пока не найдём
    if int(line) % 2 != 0:
        x = int(line)
    line = file.readline()
    print(line, end='')

min_ = x

for line in file:
    x = int(line)
    if x%2 != 0 and x<min_:
        min_ = x
    print(line, end='')

print()

if (min_ % 2 != 0):
    print('Min = ' + str(min_))
else:
    print('Число не найдено')
    
file.close()
