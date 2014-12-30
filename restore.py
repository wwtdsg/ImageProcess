# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from math import sqrt, floor

im = misc.imread('00.jpg')
height, width = im.shape  # (480, 640)


def recover(im):  # 恢复畸变算法
    res = np.zeros((height, width))
    for j in range(height):
        for i in range(width):
            ch = pow((2.0 * i - width) / width, 2) + pow((2.0 * j - height) / height, 2)
            if ch < 1:
                temp = width / 2.0 * (j - height / 2.0) / sqrt(width * i - pow(i, 2.0))
                y = height / 2.0 + temp
                x = i
                y = floor(y)
                res[y][x] = im[j][i]
    return res


def filling(im):  # 填充空白像素点
    value = [0.0] * 9
    average = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            if im[i][j] != 0:
                average[i][j] = im[i][j]
            if im[i][j] == 0:
                try:
                    value[0] = average[i - 1][j - 1]
                    value[1] = average[i - 1][j - 2]
                    value[2] = average[i - 1][j - 3]
                    value[3] = average[i - 1][j - 4]
                    value[4] = average[i - 1][j - 5]
                    value[5] = average[i - 1][j + 1]
                    value[6] = average[i - 1][j + 2]
                    value[7] = average[i - 1][j + 3]
                    value[8] = average[i - 1][j + 4]
                    for n in range(9):
                        average[i][j] += np.int(value[n])
                    average[i][j] = average[i][j] / 9.0
                except:
                    average[i][j] = im[i][j]
    return average


def smooth(im):  # 图像均值平滑
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
                average[i][j] = average[i][j] / 9.0
            except:
                average[i][j] = im[i][j]
    return average

res = smooth(filling(recover(im)))  # 这里可以选择[smooth[filling[recover]]]的图像处理组合
plt.imshow(res, cmap=plt.cm.gray)
plt.show()
