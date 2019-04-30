# coding: utf-8
from matplotlib import pyplot as plt

f_additiveData = open('C:/Users/akopo/CLionProjects/misoi2/python/additivePSNR3data', 'r')
f_additiveValue = open('C:/Users/akopo/CLionProjects/misoi2/python/additivePSNR3', 'r')

array_additiveData = []
array_additiveValue = []

for line in f_additiveData:
    array_additiveData.append([int(x) for x in line.split()])
for line in f_additiveValue:
    array_additiveValue.append([float(x) for x in line.split()])

a = array_additiveData[0][0]
step = array_additiveData[2][0]



plt.figure()
plt.plot(range(a, len(array_additiveValue[0]) * step + a, step), array_additiveValue[0], color='m')
plt.xlabel("sigma")
plt.ylabel("PSNR")


f_impulseData = open('C:/Users/akopo/CLionProjects/misoi2/python/impulsePSNR3data', 'r')
f_impulseValue = open('C:/Users/akopo/CLionProjects/misoi2/python/impulsePSNR3', 'r')

array_impulseData = []
array_impulseValue = []

for line in f_impulseData:
    array_impulseData.append([float(x) for x in line.split()])
for line in f_impulseValue:
    array_impulseValue.append([float(x) for x in line.split()])

PaR = array_impulseData[0][0]
PaL = array_impulseData[1][0]
PaS = array_impulseData[2][0] * 100



plt.figure()
plt.plot(range(0, len(array_impulseValue[0]) * int(PaS), int(PaS)), array_impulseValue[0], color='y')
plt.xlabel("P, %")
plt.ylabel("PSNR")
plt.show()