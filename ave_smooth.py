import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

im = misc.imread('lena.png')
height, width = im.shape
plt.imshow(im, cmap=plt.cm.gray)
value = [0.0] * 9
temp = [0.0] * 9
seq = [0] * 9
average = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        try:
            value[0] = im[i - 1][j - 1]
            value[1] = im[i][j - 1]
            value[2] = im[i + 1][j - 1]
            value[3] = im[i][j + 1]
            value[4] = im[i][j]
            value[5] = im[i + 1][j]
            value[6] = im[i - 1][j + 1]
            value[7] = im[i][j + 1]
            value[8] = im[i + 1][j + 1]
            for n in range(9):
                average[i][j] += np.int(value[n])
        except:
            average[i][j] = im[i][j]
plt.imshow(average, cmap=plt.cm.gray)
plt.show()
