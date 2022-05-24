from numpy import *

a = random.randint(10, size = (random.randint(1,10),random.randint(1,10)))

print(a)

print("Product of a = " + str(nanprod(a)))
print("Std of a = " + str(nanstd(a)))
print("Index of min of a = " + str(nanargmin(a)))
