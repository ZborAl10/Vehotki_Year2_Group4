from numpy.linalg import *

n = int(input("n = "))
a = [0]*n

for i in range(n):
    a[i] = [0]*n
    for j in range(n):
        a[i][j] = int(input("a[" + str(i) + "][" + str(j) + "] = "))

s = ''
for i in eig(a)[0]:
    s += str(i)
    s += ', '

s = s[:-2]

print("Eigenvalues of matrix = " + s)

s = ''
for i in eig(a)[1]:
    for j in i:
        s += str(j)
        s += ', '

s = s[:-2]

print("Eigenvectors of matrix = " + s)
