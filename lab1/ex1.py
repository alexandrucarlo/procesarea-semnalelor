# ex1
import numpy as np
import matplotlib.pyplot as plt

# punctul b
def x(t):
    return np.cos(520 * np.pi * t + np.pi / 3)

def y(t):
    return np.cos(280 * np.pi * t - np.pi / 3)

def z(t):
    return np.cos(120 * np.pi * t + np.pi / 3)
# punctul a
timp = np.linspace(0, 0.5, int(1/0.00005))
# punctul c
timp_esantion = np.arange(0, 0.5, 1/200)
n = 3

# punctul b, c
fig, axs = plt.subplots(n)
fig.suptitle('Exercitiul 1')
axs[0].plot(timp,x(timp))
axs[0].stem(timp_esantion, x(timp_esantion))
axs[1].plot(timp,y(timp))
axs[1].stem(timp_esantion, y(timp_esantion))
axs[2].plot(timp,z(timp))
axs[2].stem(timp_esantion, z(timp_esantion))
plt.show()
