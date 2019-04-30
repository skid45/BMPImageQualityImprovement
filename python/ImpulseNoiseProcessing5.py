# coding: utf-8
from skimage import io
from matplotlib import pyplot as plt


#original
plt.figure()
img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/OriginalImpulseNoiseImageWithP=0.050000.bmp')
plt.subplot(2, 2, 1)
plt.title("p = 0.05")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/OriginalImpulseNoiseImageWithP=0.100000.bmp')
plt.subplot(2, 2, 2)
plt.title("p = 0.1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/OriginalImpulseNoiseImageWithP=0.250000.bmp')
plt.subplot(2, 2, 3)
plt.title("p = 0.25")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/OriginalImpulseNoiseImageWithP=0.500000.bmp')
plt.subplot(2, 2, 4)
plt.title("p = 0.5")
plt.imshow(img)


#p=0.05
plt.figure()
img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.050000andR0.bmp')
plt.subplot(2, 3, 1)
plt.title("p = 0.05, R = 0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.050000andR1.bmp')
plt.subplot(2, 3, 2)
plt.title("p = 0.05, R = 1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.050000andR2.bmp')
plt.subplot(2, 3, 3)
plt.title("p = 0.05, R = 2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.050000andR3.bmp')
plt.subplot(2, 3, 4)
plt.title("p = 0.05, R = 3")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.050000andR4.bmp')
plt.subplot(2, 3, 5)
plt.title("p = 0.05, R = 4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.050000andR5.bmp')
plt.subplot(2, 3, 6)
plt.title("p = 0.05, R = 5")
plt.imshow(img)


#p=0.1
plt.figure()
img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.100000andR0.bmp')
plt.subplot(2, 3, 1)
plt.title("p = 0.1, R = 0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.100000andR1.bmp')
plt.subplot(2, 3, 2)
plt.title("p = 0.1, R = 1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.100000andR2.bmp')
plt.subplot(2, 3, 3)
plt.title("p = 0.1, R = 2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.100000andR3.bmp')
plt.subplot(2, 3, 4)
plt.title("p = 0.1, R = 3")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.100000andR4.bmp')
plt.subplot(2, 3, 5)
plt.title("p = 0.1, R = 4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.100000andR5.bmp')
plt.subplot(2, 3, 6)
plt.title("p = 0.1, R = 5")
plt.imshow(img)



#p=0.25
plt.figure()
img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.250000andR0.bmp')
plt.subplot(2, 3, 1)
plt.title("p = 0.25, R = 0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.250000andR1.bmp')
plt.subplot(2, 3, 2)
plt.title("p = 0.25, R = 1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.250000andR2.bmp')
plt.subplot(2, 3, 3)
plt.title("p = 0.25, R = 2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.250000andR3.bmp')
plt.subplot(2, 3, 4)
plt.title("p = 0.25, R = 3")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.250000andR4.bmp')
plt.subplot(2, 3, 5)
plt.title("p = 0.25, R = 4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.250000andR5.bmp')
plt.subplot(2, 3, 6)
plt.title("p = 0.25, R = 5")
plt.imshow(img)


#p=0.5
plt.figure()
img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.500000andR0.bmp')
plt.subplot(2, 3, 1)
plt.title("p = 0.5, R = 0")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.500000andR1.bmp')
plt.subplot(2, 3, 2)
plt.title("p = 0.5, R = 1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.500000andR2.bmp')
plt.subplot(2, 3, 3)
plt.title("p = 0.5, R = 2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.500000andR3.bmp')
plt.subplot(2, 3, 4)
plt.title("p = 0.5, R = 3")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.500000andR4.bmp')
plt.subplot(2, 3, 5)
plt.title("p = 0.5, R = 4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/ImpulseNoiseImageAfterMedianFilterWithP=0.500000andR5.bmp')
plt.subplot(2, 3, 6)
plt.title("p = 0.5, R = 5")
plt.imshow(img)

#PSNR
f_Value = open('C:/Users/akopo/CLionProjects/misoi2/python/ImpulseNoiseProcessing5', 'r')

arr_val = []

for line in f_Value:
    arr_val.append([float(x) for x in line.split()])

plt.figure()
plt.plot(range(0, len(arr_val[1])), arr_val[1], label="P=0.05")
plt.plot(range(0, len(arr_val[3])), arr_val[3], label="P=0.1")
plt.plot(range(0, len(arr_val[5])), arr_val[5], label="P=0.25")
plt.plot(range(0, len(arr_val[7])), arr_val[7], label="P=0.5")
plt.legend()
plt.title("P=0.05, PSNR зашумлённого изображения без фильтрации = " + str(arr_val[0][0]) +
          "\nP=0.1, PSNR зашумлённого изображения без фильтрации = " + str(arr_val[2][0]) +
          "\nP=0.25, PSNR зашумлённого изображения без фильтрации = " + str(arr_val[4][0]) +
          "\nP=0.5, PSNR зашумлённого изображения без фильтрации = " + str(arr_val[6][0]))
plt.xlabel("R")
plt.ylabel("PSNR")
plt.show()