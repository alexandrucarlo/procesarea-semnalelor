# ex3
import numpy as np
import sounddevice
import scipy.io.wavfile
import scipy.signal

freq = 440
samp_freq = 44100 # magic nyquist shannon
dur = 2 # secunde
def x(t, phase):
    return np.sin(freq * np.pi * t + phase)

timp = np.linspace(0, dur, samp_freq * dur) # avem nevoie de samp_freq * dur sample-uri (duh)


x4 = x(timp, np.pi * 1.5)
sounddevice.default.device = 7 # nu-mi alege bine default device-ul :p 
sounddevice.play(x4, samp_freq) 
sounddevice.wait()


z = np.random.normal(loc=0.0, scale=1.0, size=len(timp))

norm_x_sq = np.linalg.norm(x4) ** 2
norm_z_sq = np.linalg.norm(z) ** 2

snr = [0.1, 1, 10, 100]
for s in snr:
    gamma = np.sqrt(norm_x_sq / (s * norm_z_sq)) # regula de 3 simpla
    
    semnal_zgomotos = x4 + gamma * z
    
    sounddevice.play(semnal_zgomotos, samp_freq) 
    sounddevice.wait()

scipy.io.wavfile.write('ex3.wav', samp_freq, semnal_zgomotos)
print(scipy.io.wavfile.read('ex3.wav')) # afiseaza chestii deci merge
