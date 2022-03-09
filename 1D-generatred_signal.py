import numpy as np
import matplotlib.pyplot as plt

#Signal parameters:
f_sig = 10 #Signal frequency [Hz]
amplitude = 1 #[m]

#Sampling paramters
T = 20 #total time of sample [s]
f_samp = 1000 #samplingfrequency (Remember Aliasing problems) [Hz]
N = T*f_samp #Number of sampling points in a given T.
dt = T/N #timesteps, time between each sampling point.

t = np.linspace(0, T, N) #Array which holds all timesteps
sampled_func = amplitude*np.sin(2*np.pi*f_sig*t) #Sampled function which takes in signal frequency. Signalvalue for each sampled timesteps

#Fourier transformation
transformed_sampled_func = np.fft.fft(sampled_func)
freq = np.fft.fftfreq(N, dt)

print(transformed_sampled_func)


plt.plot(freq, transformed_sampled_func)
plt.show()
