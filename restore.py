import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import Image
from math import sqrt, floor

im = Image.open('1.jpg')
im = im.convert('L')
im.save('11.jpg')
im = misc.imread('11.jpg')
print im[479][639]
height, width = im.shape  # (480, 640)
res = np.zeros((height, width))
n = 0
for j in range(height):
    for i in range(width):
        ch = pow((i - 320.0) / 320.0, 2) + pow((j - 240.0) / 240, 2)
        if ch < 1:
            temp = 320.0 * (j - 240) / sqrt(640.0 * i - pow(i, 2))
            y = 240.0 + temp
            x = i
            y = floor(y)
            res[y][x] = im[j][i]

plt.imshow(res, cmap=plt.cm.gray)
plt.show()
