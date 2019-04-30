# coding: utf-8
from matplotlib import pyplot as plt
from skimage import io

f_graph = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrection', 'r')

a_graph = []

for line in f_graph:
    a_graph.append([float(x) for x in line.split()])

plt.figure()
plt.plot(range(0, len(a_graph[0])), a_graph[0], label="0.04")
plt.plot(range(0, len(a_graph[1])), a_graph[1], label="0.1")
plt.plot(range(0, len(a_graph[2])), a_graph[2], label="0.2")
plt.plot(range(0, len(a_graph[3])), a_graph[3], label="0.4")
plt.plot(range(0, len(a_graph[4])), a_graph[4], label="0.67")
plt.plot(range(0, len(a_graph[5])), a_graph[5], label="1.0")
plt.plot(range(0, len(a_graph[6])), a_graph[6], label="1.5")
plt.plot(range(0, len(a_graph[7])), a_graph[7], label="2.5")
plt.plot(range(0, len(a_graph[8])), a_graph[8], label="5.0")
plt.plot(range(0, len(a_graph[9])), a_graph[9], label="10.0")
plt.plot(range(0, len(a_graph[10])), a_graph[10], label="25.0")
plt.legend()
plt.xlabel("Входное значение")
plt.ylabel("Выходное значение")


img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage0.040000.bmp')
plt.figure()
plt.subplot(2, 3, 1)
plt.title("gamma = 0.04")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage0.100000.bmp')
plt.subplot(2, 3, 2)
plt.title("gamma = 0.1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage0.200000.bmp')
plt.subplot(2, 3, 3)
plt.title("gamma = 0.2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage0.400000.bmp')
plt.subplot(2, 3, 4)
plt.title("gamma = 0.4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage0.670000.bmp')
plt.subplot(2, 3, 5)
plt.title("gamma = 0.67")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage1.000000.bmp')
plt.subplot(2, 3, 6)
plt.title("gamma = 1.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage1.500000.bmp')
plt.figure()
plt.subplot(2, 3, 1)
plt.title("gamma = 1.5")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage2.500000.bmp')
plt.subplot(2, 3, 2)
plt.title("gamma = 2.5")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage5.000000.bmp')
plt.subplot(2, 3, 3)
plt.title("gamma = 5.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage10.000000.bmp')
plt.subplot(2, 3, 4)
plt.title("gamma = 10.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBalanceImage25.000000.bmp')
plt.subplot(2, 3, 5)
plt.title("gamma = 25.0")
plt.imshow(img)


img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage0.040000.bmp')
plt.figure()
plt.subplot(2, 3, 1)
plt.title("gamma = 0.04")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage0.100000.bmp')
plt.subplot(2, 3, 2)
plt.title("gamma = 0.1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage0.200000.bmp')
plt.subplot(2, 3, 3)
plt.title("gamma = 0.2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage0.400000.bmp')
plt.subplot(2, 3, 4)
plt.title("gamma = 0.4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage0.670000.bmp')
plt.subplot(2, 3, 5)
plt.title("gamma = 0.67")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage1.000000.bmp')
plt.subplot(2, 3, 6)
plt.title("gamma = 1.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage1.500000.bmp')
plt.figure()
plt.subplot(2, 3, 1)
plt.title("gamma = 1.5")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage2.500000.bmp')
plt.subplot(2, 3, 2)
plt.title("gamma = 2.5")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage5.000000.bmp')
plt.subplot(2, 3, 3)
plt.title("gamma = 5.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage10.000000.bmp')
plt.subplot(2, 3, 4)
plt.title("gamma = 10.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionBrightImage25.000000.bmp')
plt.subplot(2, 3, 5)
plt.title("gamma = 25.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage0.040000.bmp')
plt.figure()
plt.subplot(2, 3, 1)
plt.title("gamma = 0.04")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage0.100000.bmp')
plt.subplot(2, 3, 2)
plt.title("gamma = 0.1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage0.200000.bmp')
plt.subplot(2, 3, 3)
plt.title("gamma = 0.2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage0.400000.bmp')
plt.subplot(2, 3, 4)
plt.title("gamma = 0.4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage0.670000.bmp')
plt.subplot(2, 3, 5)
plt.title("gamma = 0.67")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage1.000000.bmp')
plt.subplot(2, 3, 6)
plt.title("gamma = 1.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage1.500000.bmp')
plt.figure()
plt.subplot(2, 3, 1)
plt.title("gamma = 1.5")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage2.500000.bmp')
plt.subplot(2, 3, 2)
plt.title("gamma = 2.5")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage5.000000.bmp')
plt.subplot(2, 3, 3)
plt.title("gamma = 5.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage10.000000.bmp')
plt.subplot(2, 3, 4)
plt.title("gamma = 10.0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/GammaCorrectionDarkImage25.000000.bmp')
plt.subplot(2, 3, 5)
plt.title("gamma = 25.0")
plt.imshow(img)

f_histBa1 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage0.040000', 'r')
f_histBa2 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage0.100000', 'r')
f_histBa3 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage0.200000', 'r')
f_histBa4 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage0.400000', 'r')
f_histBa5 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage0.670000', 'r')
f_histBa6 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage1.000000', 'r')
f_histBa7 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage1.500000', 'r')
f_histBa8 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage2.500000', 'r')
f_histBa9 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage5.000000', 'r')
f_histBa10 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage10.000000', 'r')
f_histBa11 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBalanceImage25.000000', 'r')

a_histBa1 = []
a_histBa2 = []
a_histBa3 = []
a_histBa4 = []
a_histBa5 = []
a_histBa6 = []
a_histBa7 = []
a_histBa8 = []
a_histBa9 = []
a_histBa10 = []
a_histBa11 = []

for line in f_histBa1:
    a_histBa1.append([int(x) for x in line.split()])
for line in f_histBa2:
    a_histBa2.append([int(x) for x in line.split()])
for line in f_histBa3:
    a_histBa3.append([int(x) for x in line.split()])
for line in f_histBa4:
    a_histBa4.append([int(x) for x in line.split()])
for line in f_histBa5:
    a_histBa5.append([int(x) for x in line.split()])
for line in f_histBa6:
    a_histBa6.append([int(x) for x in line.split()])
for line in f_histBa7:
    a_histBa7.append([int(x) for x in line.split()])
for line in f_histBa8:
    a_histBa8.append([int(x) for x in line.split()])
for line in f_histBa9:
    a_histBa9.append([int(x) for x in line.split()])
for line in f_histBa10:
    a_histBa10.append([int(x) for x in line.split()])
for line in f_histBa11:
    a_histBa11.append([int(x) for x in line.split()])

plt.figure()
plt.subplot(2, 3, 1)
plt.hist(a_histBa1[0], bins=range(0, 256))
plt.title("gamma = 0.04")

plt.subplot(2, 3, 2)
plt.hist(a_histBa2[0], bins=range(0, 256))
plt.title("alpha = 0.1")

plt.subplot(2, 3, 3)
plt.hist(a_histBa3[0], bins=range(0, 256))
plt.title("alpha = 0.2")

plt.subplot(2, 3, 4)
plt.hist(a_histBa4[0], bins=range(0, 256))
plt.title("alpha = 0.4")

plt.subplot(2, 3, 5)
plt.hist(a_histBa5[0], bins=range(0, 256))
plt.title("alpha = 0.67")

plt.subplot(2, 3, 6)
plt.hist(a_histBa6[0], bins=range(0, 256))
plt.title("alpha = 1.0")

plt.figure()
plt.subplot(2, 3, 1)
plt.hist(a_histBa7[0], bins=range(0, 256))
plt.title("gamma = 1.5")

plt.subplot(2, 3, 2)
plt.hist(a_histBa8[0], bins=range(0, 256))
plt.title("alpha = 2.5")

plt.subplot(2, 3, 3)
plt.hist(a_histBa9[0], bins=range(0, 256))
plt.title("alpha = 5.0")

plt.subplot(2, 3, 4)
plt.hist(a_histBa10[0], bins=range(0, 256))
plt.title("alpha = 10.0")

plt.subplot(2, 3, 5)
plt.hist(a_histBa11[0], bins=range(0, 256))
plt.title("alpha = 25.0")


f_histBr1 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage0.040000', 'r')
f_histBr2 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage0.100000', 'r')
f_histBr3 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage0.200000', 'r')
f_histBr4 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage0.400000', 'r')
f_histBr5 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage0.670000', 'r')
f_histBr6 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage1.000000', 'r')
f_histBr7 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage1.500000', 'r')
f_histBr8 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage2.500000', 'r')
f_histBr9 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage5.000000', 'r')
f_histBr10 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage10.000000', 'r')
f_histBr11 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionBrightImage25.000000', 'r')

a_histBr1 = []
a_histBr2 = []
a_histBr3 = []
a_histBr4 = []
a_histBr5 = []
a_histBr6 = []
a_histBr7 = []
a_histBr8 = []
a_histBr9 = []
a_histBr10 = []
a_histBr11 = []

for line in f_histBr1:
    a_histBr1.append([int(x) for x in line.split()])
for line in f_histBr2:
    a_histBr2.append([int(x) for x in line.split()])
for line in f_histBr3:
    a_histBr3.append([int(x) for x in line.split()])
for line in f_histBr4:
    a_histBr4.append([int(x) for x in line.split()])
for line in f_histBr5:
    a_histBr5.append([int(x) for x in line.split()])
for line in f_histBr6:
    a_histBr6.append([int(x) for x in line.split()])
for line in f_histBr7:
    a_histBr7.append([int(x) for x in line.split()])
for line in f_histBr8:
    a_histBr8.append([int(x) for x in line.split()])
for line in f_histBr9:
    a_histBr9.append([int(x) for x in line.split()])
for line in f_histBr10:
    a_histBr10.append([int(x) for x in line.split()])
for line in f_histBr11:
    a_histBr11.append([int(x) for x in line.split()])

plt.figure()
plt.subplot(2, 3, 1)
plt.hist(a_histBr1[0], bins=range(0, 256))
plt.title("gamma = 0.04")

plt.subplot(2, 3, 2)
plt.hist(a_histBr2[0], bins=range(0, 256))
plt.title("alpha = 0.1")

plt.subplot(2, 3, 3)
plt.hist(a_histBr3[0], bins=range(0, 256))
plt.title("alpha = 0.2")

plt.subplot(2, 3, 4)
plt.hist(a_histBr4[0], bins=range(0, 256))
plt.title("alpha = 0.4")

plt.subplot(2, 3, 5)
plt.hist(a_histBr5[0], bins=range(0, 256))
plt.title("alpha = 0.67")

plt.subplot(2, 3, 6)
plt.hist(a_histBr6[0], bins=range(0, 256))
plt.title("alpha = 1.0")

plt.figure()
plt.subplot(2, 3, 1)
plt.hist(a_histBr7[0], bins=range(0, 256))
plt.title("gamma = 1.5")

plt.subplot(2, 3, 2)
plt.hist(a_histBr8[0], bins=range(0, 256))
plt.title("alpha = 2.5")

plt.subplot(2, 3, 3)
plt.hist(a_histBr9[0], bins=range(0, 256))
plt.title("alpha = 5.0")

plt.subplot(2, 3, 4)
plt.hist(a_histBr10[0], bins=range(0, 256))
plt.title("alpha = 10.0")

plt.subplot(2, 3, 5)
plt.hist(a_histBr11[0], bins=range(0, 256))
plt.title("alpha = 25.0")


f_histD1 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage0.040000', 'r')
f_histD2 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage0.100000', 'r')
f_histD3 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage0.200000', 'r')
f_histD4 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage0.400000', 'r')
f_histD5 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage0.670000', 'r')
f_histD6 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage1.000000', 'r')
f_histD7 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage1.500000', 'r')
f_histD8 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage2.500000', 'r')
f_histD9 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage5.000000', 'r')
f_histD10 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage10.000000', 'r')
f_histD11 = open('C:/Users/akopo/CLionProjects/misoi2/python/GammaCorrectionDarkImage25.000000', 'r')

a_histD1 = []
a_histD2 = []
a_histD3 = []
a_histD4 = []
a_histD5 = []
a_histD6 = []
a_histD7 = []
a_histD8 = []
a_histD9 = []
a_histD10 = []
a_histD11 = []

for line in f_histD1:
    a_histD1.append([int(x) for x in line.split()])
for line in f_histD2:
    a_histD2.append([int(x) for x in line.split()])
for line in f_histD3:
    a_histD3.append([int(x) for x in line.split()])
for line in f_histD4:
    a_histD4.append([int(x) for x in line.split()])
for line in f_histD5:
    a_histD5.append([int(x) for x in line.split()])
for line in f_histD6:
    a_histD6.append([int(x) for x in line.split()])
for line in f_histD7:
    a_histD7.append([int(x) for x in line.split()])
for line in f_histD8:
    a_histD8.append([int(x) for x in line.split()])
for line in f_histD9:
    a_histD9.append([int(x) for x in line.split()])
for line in f_histD10:
    a_histD10.append([int(x) for x in line.split()])
for line in f_histD11:
    a_histD11.append([int(x) for x in line.split()])

plt.figure()
plt.subplot(2, 3, 1)
plt.hist(a_histD1[0], bins=range(0, 256))
plt.title("gamma = 0.04")

plt.subplot(2, 3, 2)
plt.hist(a_histD2[0], bins=range(0, 256))
plt.title("alpha = 0.1")

plt.subplot(2, 3, 3)
plt.hist(a_histD3[0], bins=range(0, 256))
plt.title("alpha = 0.2")

plt.subplot(2, 3, 4)
plt.hist(a_histD4[0], bins=range(0, 256))
plt.title("alpha = 0.4")

plt.subplot(2, 3, 5)
plt.hist(a_histD5[0], bins=range(0, 256))
plt.title("alpha = 0.67")

plt.subplot(2, 3, 6)
plt.hist(a_histD6[0], bins=range(0, 256))
plt.title("alpha = 1.0")

plt.figure()
plt.subplot(2, 3, 1)
plt.hist(a_histD7[0], bins=range(0, 256))
plt.title("gamma = 1.5")

plt.subplot(2, 3, 2)
plt.hist(a_histD8[0], bins=range(0, 256))
plt.title("alpha = 2.5")

plt.subplot(2, 3, 3)
plt.hist(a_histD9[0], bins=range(0, 256))
plt.title("alpha = 5.0")

plt.subplot(2, 3, 4)
plt.hist(a_histD10[0], bins=range(0, 256))
plt.title("alpha = 10.0")

plt.subplot(2, 3, 5)
plt.hist(a_histD11[0], bins=range(0, 256))
plt.title("alpha = 25.0")

plt.show()