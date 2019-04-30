# coding: utf-8
from matplotlib import pyplot as plt


f_hist = open('C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseHist', 'r')

array_hist = []

for line in f_hist:
    array_hist.append([int(x) for x in line.split()])

plt.figure()
plt.hist(array_hist[0], bins=range(0, 256))
plt.show()
