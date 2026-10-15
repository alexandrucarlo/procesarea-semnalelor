import numpy as np
import matplotlib.pyplot as plt

# punctul a
def x(t):
    freq = 400
    return np.sin(freq*2 * np.pi * t) # nu avem destule esantioane, apare aliasing

# punctul b
def y(t):
    return np.where(t > 3, 0, np.sin(800 * 2 * np.pi * t - np.pi / 3))

# punctul c
def z(t):
    freq = 240
    phase = 1/2
    #return np.mod((t + 1/2), 1/freq) * 2 * freq - 1 # todo shiftarea fazei, nu merge pe pare!!
    return 2 * (freq * t - np.floor(freq * t + phase)) # mersi wikipedia :p

#punctul d
def w(t):
    freq = 3
    phase = 0
    signal = np.sign(np.sin(freq * 2 * np.pi * t + phase)) # prima valoare va fi 0 pt ca asa functioneaza sign..... dar mi-e prea lene sa folosesc np.where
    signal[0] = 1
    return signal

a = np.linspace(0, 0.5*np.pi, 128) # cand ma enerveaza trigonometria imi place sa ma gandesc ca pi vine de la paul irofti

# punctul e
img_1 = np.random.rand(128,128)
# punctul f
img_2 = np.tan(np.sin(a[:, None] + a[None, ::-1]))


timp = np.linspace(0, 1, int(1/0.00005))
timp_b = np.linspace(0, 4, int(1/0.00001))
timp_esantion = np.linspace(0, 1, 1600)
n = 4
fig, axs = plt.subplots(n)
fig.suptitle('Exercitiul 2: semnale 1D')
# punctul a
axs[0].stem(timp_esantion, x(timp_esantion))
#punctul b
axs[1].plot(timp_b,y(timp_b))
# punctul c
axs[2].plot(timp,z(timp))
# punctul d
axs[3].plot(timp,w(timp))
# punctul e
plt.show()

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 2: 2D')
axs[0].imshow(img_1)
axs[1].imshow(img_2)
plt.show()
