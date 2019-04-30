# coding: utf-8
from matplotlib import pyplot as plt
from skimage import io

f_graph = open('C:/Users/akopo/CLionProjects/misoi2/python/TwoReferencePointsGraph', 'r')

a_graph = []

for line in f_graph:
    a_graph.append([float(x) for x in line.split()])

plt.figure()
plt.plot(range(0, len(a_graph[0])), a_graph[0])
plt.xlabel("Входное значение")
plt.ylabel("Выходное значение")


img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/BalanceY.bmp')
plt.figure()
plt.subplot(2, 2, 1)
plt.title("Исходное изображение")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/BalanceTwoReferencePoints.bmp')
plt.subplot(2, 2, 2)
plt.title("Изображение после преобразования")
plt.imshow(img)

f_histBa1 = open('C:/Users/akopo/CLionProjects/misoi2/python/BalanceOriginalHist', 'r')
f_histBa2 = open('C:/Users/akopo/CLionProjects/misoi2/python/BalanceTwoReferencePointsHist', 'r')

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
plt.title("Гистограмма изображения после преобразования")
plt.hist(a_histBa2[0], bins=range(0, 256))



img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/BrightY.bmp')
plt.figure()
plt.subplot(2, 2, 1)
plt.title("Исходное изображение")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/BrightTwoReferencePoints.bmp')
plt.subplot(2, 2, 2)
plt.title("Изображение после преобразования")
plt.imshow(img)

f_histBr1 = open('C:/Users/akopo/CLionProjects/misoi2/python/BrightOriginalHist', 'r')
f_histBr2 = open('C:/Users/akopo/CLionProjects/misoi2/python/BrightTwoReferencePointsHist', 'r')

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
plt.title("Гистограмма изображения после преобразования")
plt.hist(a_histBr2[0], bins=range(0, 256))




img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/DarkY.bmp')
plt.figure()
plt.subplot(2, 2, 1)
plt.title("Исходное изображение")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/DarkTwoReferencePoints.bmp')
plt.subplot(2, 2, 2)
plt.title("Изображение после преобразования")
plt.imshow(img)

f_histD1 = open('C:/Users/akopo/CLionProjects/misoi2/python/DarkOriginalHist', 'r')
f_histD2 = open('C:/Users/akopo/CLionProjects/misoi2/python/DarkTwoReferencePointsHist', 'r')

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
plt.title("Гистограмма изображения после преобразования")
plt.hist(a_histD2[0], bins=range(0, 256))


plt.show()