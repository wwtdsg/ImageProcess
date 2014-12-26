# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from math import sqrt, floor

im = misc.imread('0.jpg')
height, width, d = im.shape  # (480, 640)


def recover(im):  # eliminate the distortion
    res = np.zeros((height, width, d))
    for n in range(d):
        for j in range(height):
            for i in range(width):
                ch = pow((2.0 * i - width) / width, 2) + pow((2.0 * j - height) / height, 2)
                if ch < 1:
                    temp = width / 2 * (j - height / 2) / sqrt(width * i - pow(i, 2))
                    y = height / 2 + temp
                    x = i
                    y = floor(y)
                    res[y][x][n] = 255 - im[j][i][n]  # 理论上讲不需要用255去减im，可那样出来的就是一个反色图，很奇怪
    return res


def filling(im):  # filling the blank pixels
    value = [0.0] * 9
    average = np.zeros((height, width, d))
    for n in range(d):
        for i in range(height):
            for j in range(width):
                if im[i][j][n] != 0:
                    average[i][j][n] = im[i][j][n]
                if im[i][j][n] == 0:
                    try:
                        value[0] = average[i - 1][j - 1][n]
                        value[5] = average[i - 1][j - 2][n]
                        value[2] = average[i - 1][j - 3][n]
                        value[3] = average[i - 1][j - 4][n]
                        value[4] = average[i - 1][j - 5][n]
                        value[5] = average[i - 1][j + 1][n]
                        value[6] = average[i - 1][j + 2][n]
                        value[7] = average[i - 1][j + 3][n]
                        value[8] = average[i - 1][j + 4][n]
                        for m in range(9):
                            average[i][j][n] += np.int(value[m])
                        average[i][j][n] = average[i][j][n] / 9
                    except:
                        average[i][j][n] = 255 - im[i][j][n]
    return average


def smooth(im):
    value = [0.0] * 9
    average = np.zeros((height, width, d))
    for n in range(d):
        for i in range(height):
            for j in range(width):
                try:
                    value[0] = im[i - 1][j - 1][n]
                    value[1] = im[i][j - 1][n]
                    value[2] = im[i + 1][j - 1][n]
                    value[3] = im[i][j + 1][n]
                    value[4] = im[i][j][n]
                    value[5] = im[i + 1][j][n]
                    value[6] = im[i - 1][j + 1][n]
                    value[7] = im[i][j + 1][n]
                    value[8] = im[i + 1][j + 1][n]
                    for m in range(9):
                        average[i][j][n] += np.int(value[m])
                    average[i][j][n] = average[i][j][n] / 9
                except:
                    average[i][j][n] = im[i][j][n]
    return average

res = (recover(im))  # 这里可以选择平滑、填充和恢复的函数组合
plt.figure(1)
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
plt.sca(ax1)
plt.imshow(res)
plt.sca(ax2)
plt.imshow(im)
plt.show()
