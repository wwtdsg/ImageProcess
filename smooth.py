import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


def seqence(temped, temp):
    seq = [0] * 9
    for m in range(9):
                for x in range(9):
                    if temped[m] == temp[x]:
                        temp[x] = 100
                        seq[m] = x
                        break
    return seq

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
                temp[n] = np.abs(np.int(value[n]) - np.int(value[4]))
            temped = sorted(temp)
            seq = seqence(temped, temp)
            total = (np.int(value[seq[0]]) + np.int(value[seq[6]]) + np.int(value[seq[1]]) + np.int(value[seq[2]]) + np.int(value[seq[3]]) + np.int(value[seq[4]]) + np.int(value[seq[5]])) / 7
            average[i][j] = total
        except:
            average[i][j] = im[i][j]
plt.imshow(average, cmap=plt.cm.gray)
plt.show()
