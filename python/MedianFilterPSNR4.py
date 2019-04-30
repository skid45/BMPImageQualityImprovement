# coding: utf-8
from matplotlib import pyplot as plt

f_Value = open('C:/Users/akopo/CLionProjects/misoi2/python/MedianFilterPSNR4', 'r')

arr_val = []

for line in f_Value:
    arr_val.append([float(x) for x in line.split()])

plt.figure()
plt.plot(range(0, len(arr_val[0])), arr_val[0], color='m')
plt.title("Медианный фильтр\n" + "При R = " + str(arr_val[0].index(max(arr_val[0]))) + ", наблюдается максимальное значение PSNR = " + str(max(arr_val[0])))
plt.xlabel("R")
plt.ylabel("PSNR")
plt.show()