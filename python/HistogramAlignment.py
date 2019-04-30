# coding: utf-8
from matplotlib import pyplot as plt
from skimage import io


img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/BalanceY.bmp')
plt.figure()
plt.subplot(2, 2, 1)
plt.title("Исходное изображение")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/BalanceHAlignment.bmp')
plt.subplot(2, 2, 2)
plt.title("Изображение после выравнивания")
plt.imshow(img)

f_histBa1 = open('C:/Users/akopo/CLionProjects/misoi2/python/BalanceOriginalHist', 'r')
f_histBa2 = open('C:/Users/akopo/CLionProjects/misoi2/python/BalanceHAlignmentHist', 'r')

a_histBa1 = []
a_histBa2 = []

for line in f_histBa1:
    a_histBa1.append([int(x) for x in line.split()])
for line in f_histBa2:
    a_histBa2.append([int(x) for x in line.split()])


plt.subplot(2, 2, 3)
plt.title("Гистограмма исходного изображения")
plt.hist(a_histBa1[0], bins=range(0, 256))

plt.subplot(2, 2, 4)
plt.title("Гистограмма изображения после выравнивания")
plt.hist(a_histBa2[0], bins=range(0, 256))



img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/BrightY.bmp')
plt.figure()
plt.subplot(2, 2, 1)
plt.title("Исходное изображение")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/BrightHAlignment.bmp')
plt.subplot(2, 2, 2)
plt.title("Изображение после выравнивания")
plt.imshow(img)

f_histBr1 = open('C:/Users/akopo/CLionProjects/misoi2/python/BrightOriginalHist', 'r')
f_histBr2 = open('C:/Users/akopo/CLionProjects/misoi2/python/BrightHAlignmentHist', 'r')

a_histBr1 = []
a_histBr2 = []

for line in f_histBr1:
    a_histBr1.append([int(x) for x in line.split()])
for line in f_histBr2:
    a_histBr2.append([int(x) for x in line.split()])


plt.subplot(2, 2, 3)
plt.title("Гистограмма исходного изображения")
plt.hist(a_histBr1[0], bins=range(0, 256))

plt.subplot(2, 2, 4)
plt.title("Гистограмма изображения после выравнивания")
plt.hist(a_histBr2[0], bins=range(0, 256))




img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/DarkY.bmp')
plt.figure()
plt.subplot(2, 2, 1)
plt.title("Исходное изображение")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/DarkHAlignment.bmp')
plt.subplot(2, 2, 2)
plt.title("Изображение после выравнивания")
plt.imshow(img)

f_histD1 = open('C:/Users/akopo/CLionProjects/misoi2/python/DarkOriginalHist', 'r')
f_histD2 = open('C:/Users/akopo/CLionProjects/misoi2/python/DarkHAlignmentHist', 'r')

a_histD1 = []
a_histD2 = []

for line in f_histD1:
    a_histD1.append([int(x) for x in line.split()])
for line in f_histD2:
    a_histD2.append([int(x) for x in line.split()])


plt.subplot(2, 2, 3)
plt.title("Гистограмма исходного изображения")
plt.hist(a_histD1[0], bins=range(0, 256))

plt.subplot(2, 2, 4)
plt.title("Гистограмма изображения после выравнивания")
plt.hist(a_histD2[0], bins=range(0, 256))


plt.show()