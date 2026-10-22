# ex2
import numpy as np
import matplotlib.pyplot as plt

freq = 440
def x(t, phase):
    return np.sin(freq * np.pi * t + phase)

timp = np.linspace(0, 0.05, int(1/0.00005)) # putin zoom fata de ex1
n = 5

fig, axs = plt.subplots(n)
fig.suptitle('Exercitiul 2')
axs[0].plot(timp,x(timp,0))
axs[0].plot(timp,x(timp,np.pi))
axs[0].plot(timp,x(timp,np.pi / 2))
axs[0].plot(timp,x(timp,np.pi * 1.5))

x4 = x(timp, np.pi * 1.5)

z = np.random.normal(loc=0.0, scale=1.0, size=len(timp))

norm_x_sq = np.linalg.norm(x4) ** 2
norm_z_sq = np.linalg.norm(z) ** 2

snr = [0.1, 1, 10, 100]
i = 1
for s in snr:
    gamma = np.sqrt(norm_x_sq / (s * norm_z_sq)) # regula de 3 simpla
    
    semnal_zgomotos = x4 + gamma * z
    
    axs[i].plot(timp, semnal_zgomotos)
    i += 1


plt.show()
