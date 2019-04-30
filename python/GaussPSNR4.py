# coding: utf-8
from skimage import io
from matplotlib import pyplot as plt

f_d = open('C:/Users/akopo/CLionProjects/misoi2/python/GaussFilterPSNR4data', 'r')
f_v = open('C:/Users/akopo/CLionProjects/misoi2/python/GaussFilterPSNR4', 'r')

arr_v = []
arr_d = []

for line in f_d:
    arr_d.append([float(x) for x in line.split()])
for line in f_v:
    arr_v.append([float(x) for x in line.split()])

plt.figure()
plt.plot(range(0, len(arr_v[0])), arr_v[0], label="R=1, лучший PSNR=" + str(max(arr_v[0])))
plt.plot(range(0, len(arr_v[1])), arr_v[2], label="R=2, лучший PSNR=" + str(max(arr_v[1])))
plt.plot(range(0, len(arr_v[2])), arr_v[2], label="R=3, лучший PSNR=" + str(max(arr_v[2])))
plt.title("Фильтр Гаусса")
plt.xlabel("sigma")
plt.ylabel("PSNR")
plt.legend()
plt.show()