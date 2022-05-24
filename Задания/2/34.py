import pickle
from random import randint

F = open('f.pkl', 'wb')
n = int(input('Количество элементов множества :'))
d = set()
for i in range(0,n) :
    d.add(randint(-100,100))
pickle.dump(d, F)
F.close()

F = open('f.pkl', 'rb')
x = pickle.load(F)
print("Произвольное множество :",x)
F.close()
