# ex1
import numpy as np
import matplotlib.pyplot as plt

freq = 440
def x(t):
    return np.sin(freq * np.pi * t + 0)

def y(t):
    return np.cos(freq * np.pi * t - np.pi/2) # diferenta de faza intre sin si cos
timp = np.linspace(0, 0.5, int(1/0.00005))
n = 2

fig, axs = plt.subplots(n)
fig.suptitle('Exercitiul 1')
axs[0].plot(timp,x(timp))
axs[1].plot(timp,y(timp))
plt.show()
