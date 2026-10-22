# ex7
import numpy as np
import matplotlib.pyplot as plt

freq = 1000 

def x(t):
    return np.sin(2 * np.pi * freq * t + 0)

timp = np.linspace(0, 0.05, int(1/0.00002))
n = 3
timp_es = timp[::4]
y = x(timp)[::4]
z = x(timp)[1::4]


fig, axs = plt.subplots(n)
fig.suptitle('Exercitiul 7')
axs[0].plot(timp,x(timp))
axs[1].plot(timp_es,y)
axs[2].plot(timp_es,z)
# iar nu cred ca am facut bine, nu pare sa se schimbe nimic???
plt.show()
