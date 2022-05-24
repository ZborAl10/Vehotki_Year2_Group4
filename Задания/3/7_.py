import numpy as np

a = np.arange(10)
print("Исходный массив :",a)

s1 = a[1:3]
s1[:] = [10,20]
s2 = a[5:6]
s2[:] = 50
s3 = a[-2:-1]
s3[:] = 80
print("Измененный массив :",a)
