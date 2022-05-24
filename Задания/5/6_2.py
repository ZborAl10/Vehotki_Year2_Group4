import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 50)
y = x**3 - x**2 - 22*x + 40
plt.title("Задание 6.2")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, label="y = x^3 - x^2 - 22x + 40")
plt.legend()
plt.show()
