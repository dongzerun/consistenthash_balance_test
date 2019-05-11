#!/bin/env python3
#coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
x = [3, 10, 50, 100, 200, 400, 600, 800, 1000]
mur = [73.918000, 131.962000, 38.078000, 30.940000, 27.720000, 16.124000, 11.568000, 8.154000, 9.064000]
city = [175.604000, 118.086000, 58.040000, 23.866000, 20.238000, 12.476000, 14.312000, 10.076000, 9.970000]
crc32 = [146.450000, 58.886000, 23.098000, 42.104000, 47.348000, 43.444000, 51.614000, 48.826000, 45.612000]
fnv1 = [743.978000, 434.380000, 93.578000, 24.586000, 14.648000, 9.394000, 8.252000, 11.584000, 12.252000]

plt.plot(x, mur, c="red", label="mur")
plt.plot(x, city, c="blue", label="city")
plt.plot(x, crc32, c="black", label="crc32")
plt.plot(x, fnv1, c="green", label="fnv1")

plt.legend(loc='upper right')
plt.grid(True)
# plt.axis('tight')
plt.xlabel('replica')
plt.ylabel('diff ratio')
plt.title('contribute diff ratio')

plt.show()