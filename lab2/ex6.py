# ex6
import numpy as np
import matplotlib.pyplot as plt

freq = 20 # alegem si noi o frecventa pe care sa nu o auda doar tantarii

def x(t):
    return np.sin(2 * np.pi * (freq/2) * t + 0)
def y(t):
    return np.sin(2 * np.pi * (freq/4) * t + 0)
def z(t):
    return np.sin(0 * np.pi * t + 0)

timp = np.arange(0, 1, 1/freq)
n = 3

fig, axs = plt.subplots(n)
fig.suptitle('Exercitiul 6')
axs[0].plot(timp,x(timp)) # aici am fp error dar e practic 0 :p
axs[1].plot(timp,y(timp)) # aici merge intre 1 si -1 mereu 
axs[2].plot(timp,z(timp))
# nu cred ca am facut bine, ar fi trebuit sa am pe prima functie numai 0, si pe a doua numai 1 si -1???????
# nevermind nu faceam array-ul de timp cum trebuie
plt.show()
