import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import Image
from math import sqrt, floor

im = Image.open('0.jpg')
im = im.convert('L')
im.save('00.jpg')
im = misc.imread('00.jpg')
height, width = im.shape  # (480, 640)


def recover(im):
    res = np.zeros((height, width))
    for j in range(height):
        for i in range(width):
            ch = pow((i - 320.0) / 320.0, 2) + pow((j - 240.0) / 240, 2)
            if ch < 1:
                temp = 320.0 * (j - 240) / sqrt(640.0 * i - pow(i, 2))
                y = 240.0 + temp
                x = i
                y = floor(y)
                res[y][x] = im[j][i]
    return res


def filling(im):
    value = [0.0] * 9
    average = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            if im[i][j] != 0:
                average[i][j] = im[i][j]
            if im[i][j] == 0:
                try:
                    value[0] = average[i - 1][j - 1]
                    value[5] = average[i - 1][j - 2]
                    value[2] = average[i - 1][j - 3]
                    value[3] = average[i - 1][j - 4]
                    value[4] = average[i - 1][j - 5]
                    value[5] = average[i - 1][j + 1]
                    value[6] = average[i - 1][j + 2]
                    value[7] = average[i - 1][j + 3]
                    value[8] = average[i - 1][j + 4]
#                    print value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8]
                    for n in range(9):
                        average[i][j] += np.int(value[n])
                    average[i][j] = average[i][j] / 9
                except:
                    average[i][j] = im[i][j]
    return average


def smooth(im):
    value = [0.0] * 9
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
                average[i][j] = average[i][j] / 9
            except:
                average[i][j] = im[i][j]
    return average

res = smooth(filling(recover(im)))
plt.imshow(res, cmap=plt.cm.gray)
plt.show()
