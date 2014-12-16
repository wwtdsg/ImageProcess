import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft

N = 500.0
fs = 50.0
t = np.arange(0, (N - 1)) / fs
f = np.arange(0, (N - 1)) * fs / N
x = np.sin(2 * np.pi * 20 * t)
y = np.abs(fft.fft(x))
f = f[1:(N / 2)]
y = y[1:(N / 2)]
plt.figure(1)
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
plt.sca(ax1)
plt.plot(t, x)
plt.sca(ax2)
plt.plot(f, y)
plt.show()
