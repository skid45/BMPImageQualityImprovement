# coding: utf-8
from skimage import io
from matplotlib import pyplot as plt

plt.figure()
img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/AdditiveNoise0.bmp')
plt.subplot(2, 2, 1)
plt.title("sigma = 0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/AdditiveNoise1.bmp')
plt.subplot(2, 2, 2)
plt.title("sigma = 15")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/AdditiveNoise2.bmp')
plt.subplot(2, 2, 3)
plt.title("sigma = 30")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/AdditiveNoise3.bmp')
plt.subplot(2, 2, 4)
plt.title("sigma = 45")
plt.imshow(img)

plt.figure()
img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/AdditiveNoise4.bmp')
plt.subplot(2, 2, 1)
plt.title("sigma = 60")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/AdditiveNoise5.bmp')
plt.subplot(2, 2, 2)
plt.title("sigma = 75")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/AdditiveNoise6.bmp')
plt.subplot(2, 2, 3)
plt.title("sigma = 90")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/AdditiveNoise7.bmp')
plt.subplot(2, 2, 4)
plt.title("sigma = 105")
plt.imshow(img)


f_histAdd0 = open('C:/Users/akopo/CLionProjects/misoi2/python/AdditiveNoiseHist0', 'r')
f_histAdd1 = open('C:/Users/akopo/CLionProjects/misoi2/python/AdditiveNoiseHist1', 'r')
f_histAdd2 = open('C:/Users/akopo/CLionProjects/misoi2/python/AdditiveNoiseHist2', 'r')
f_histAdd3 = open('C:/Users/akopo/CLionProjects/misoi2/python/AdditiveNoiseHist3', 'r')
f_histAdd4 = open('C:/Users/akopo/CLionProjects/misoi2/python/AdditiveNoiseHist4', 'r')
f_histAdd5 = open('C:/Users/akopo/CLionProjects/misoi2/python/AdditiveNoiseHist5', 'r')
f_histAdd6 = open('C:/Users/akopo/CLionProjects/misoi2/python/AdditiveNoiseHist6', 'r')
f_histAdd7 = open('C:/Users/akopo/CLionProjects/misoi2/python/AdditiveNoiseHist7', 'r')

f_histImp0 = open('C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseHist0', 'r')
f_histImp1 = open('C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseHist1', 'r')
f_histImp2 = open('C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseHist2', 'r')
f_histImp3 = open('C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseHist3', 'r')
f_histImp4 = open('C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseHist4', 'r')
f_histImp5 = open('C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseHist5', 'r')

a_histAdd0 = []
a_histAdd1 = []
a_histAdd2 = []
a_histAdd3 = []
a_histAdd4 = []
a_histAdd5 = []
a_histAdd6 = []
a_histAdd7 = []

a_histImp0 = []
a_histImp1 = []
a_histImp2 = []
a_histImp3 = []
a_histImp4 = []
a_histImp5 = []


for line in f_histAdd0:
    a_histAdd0.append([int(x) for x in line.split()])
for line in f_histAdd1:
    a_histAdd1.append([int(x) for x in line.split()])
for line in f_histAdd2:
    a_histAdd2.append([int(x) for x in line.split()])
for line in f_histAdd3:
    a_histAdd3.append([int(x) for x in line.split()])
for line in f_histAdd4:
    a_histAdd4.append([int(x) for x in line.split()])
for line in f_histAdd5:
    a_histAdd5.append([int(x) for x in line.split()])
for line in f_histAdd6:
    a_histAdd6.append([int(x) for x in line.split()])
for line in f_histAdd7:
    a_histAdd7.append([int(x) for x in line.split()])


for line in f_histImp0:
    a_histImp0.append([int(x) for x in line.split()])
for line in f_histImp1:
    a_histImp1.append([int(x) for x in line.split()])
for line in f_histImp2:
    a_histImp2.append([int(x) for x in line.split()])
for line in f_histImp3:
    a_histImp3.append([int(x) for x in line.split()])
for line in f_histImp4:
    a_histImp4.append([int(x) for x in line.split()])
for line in f_histImp5:
    a_histImp5.append([int(x) for x in line.split()])



plt.figure()
plt.subplot(2, 2, 1)
plt.hist(a_histAdd0[0], bins=range(-256, 256))
plt.title("sigma = 0")

plt.subplot(2, 2, 2)
plt.hist(a_histAdd1[0], bins=range(-256, 256))
plt.title("sigma = 15")

plt.subplot(2, 2, 3)
plt.hist(a_histAdd2[0], bins=range(-256, 256))
plt.title("sigma = 30")

plt.subplot(2, 2, 4)
plt.hist(a_histAdd3[0], bins=range(-256, 256))
plt.title("sigma = 45")

plt.figure()
plt.subplot(2, 2, 1)
plt.hist(a_histAdd4[0], bins=range(-256, 256))
plt.title("sigma = 60")

plt.subplot(2, 2, 2)
plt.hist(a_histAdd5[0], bins=range(-256, 256))
plt.title("sigma = 75")

plt.subplot(2, 2, 3)
plt.hist(a_histAdd6[0], bins=range(-256, 256))
plt.title("sigma = 90")

plt.subplot(2, 2, 4)
plt.hist(a_histAdd7[0], bins=range(-256, 256))
plt.title("sigma = 105")





plt.figure()
img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoise0.bmp')
plt.subplot(2, 3, 1)
plt.title("P = 0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoise1.bmp')
plt.subplot(2, 3, 2)
plt.title("P = 0.1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoise2.bmp')
plt.subplot(2, 3, 3)
plt.title("P = 0.2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoise3.bmp')
plt.subplot(2, 3, 4)
plt.title("P = 0.3")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoise4.bmp')
plt.subplot(2, 3, 5)
plt.title("P = 0.4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoise5.bmp')
plt.subplot(2, 3, 6)
plt.title("P = 0.5")
plt.imshow(img)


plt.figure()
plt.subplot(2, 3, 1)
plt.hist(a_histImp0[0], bins=range(0, 256))
plt.title("P = 0")

plt.subplot(2, 3, 2)
plt.hist(a_histImp1[0], bins=range(0, 256))
plt.title("P = 0.1")

plt.subplot(2, 3, 3)
plt.hist(a_histImp2[0], bins=range(0, 256))
plt.title("P = 0.2")

plt.subplot(2, 3, 4)
plt.hist(a_histImp3[0], bins=range(0, 256))
plt.title("P = 0.3")

plt.subplot(2, 3, 5)
plt.hist(a_histImp4[0], bins=range(0, 256))
plt.title("P = 0.4")

plt.subplot(2, 3, 6)
plt.hist(a_histImp5[0], bins=range(0, 256))
plt.title("P = 0.5")

plt.show()