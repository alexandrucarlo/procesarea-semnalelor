#ex5
import numpy as np
import matplotlib.pyplot as plt
import sounddevice

def x(t):
    freq = 400
    return np.sin(freq*2 * np.pi * t) 

def w(t): # luate din lab1
    freq = 600
    phase = 0
    signal = np.sign(np.sin(freq * 2 * np.pi * t + phase)) # prima valoare va fi 0 pt ca asa functioneaza sign..... dar mi-e prea lene sa folosesc np.where
    signal[0] = 1
    return signal


timp = np.linspace(0, 0.1, int(1/0.0005))
n = 3

# sa ascultam si noi
samp_freq = 44100
timp_audio = np.linspace(0, 2, samp_freq*2)
audio = x(timp_audio) + w(timp_audio)
sounddevice.default.device = 7 # nu-mi alege bine default device-ul :p 
sounddevice.play(audio, samp_freq) 
sounddevice.wait()

fig, axs = plt.subplots(n)
fig.suptitle('Exercitiul 5')
axs[0].plot(timp, x(timp))
axs[1].plot(timp, w(timp))
axs[2].plot(timp, x(timp) + w(timp))

plt.show()

