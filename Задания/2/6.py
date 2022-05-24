f=open('6.txt')
line = f.readline( )
n = line.split(' ')
num = [int(el) for el in n]
p = 1
for el in num:
    if el > 0:
        p*=el
print('Произведение положительных чисел из файла :',p)
f.close()
