from skimage import io
from matplotlib import pyplot as plt

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/laplasHFGalpha=1.000000.bmp')
plt.figure()
plt.subplot(2, 3, 1)
plt.title("alpha = 1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/laplasHFGalpha=1.100000.bmp')
plt.subplot(2, 3, 2)
plt.title("alpha = 1.1")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/laplasHFGalpha=1.200000.bmp')
plt.subplot(2, 3, 3)
plt.title("alpha = 1.2")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/laplasHFGalpha=1.300000.bmp')
plt.subplot(2, 3, 4)
plt.title("alpha = 1.3")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/laplasHFGalpha=1.400000.bmp')
plt.subplot(2, 3, 5)
plt.title("alpha = 1.4")
plt.imshow(img)

img = io.imread('C:/Users/akopo/CLionProjects/misoi2/Images/laplasHFGalpha=1.500000.bmp')
plt.subplot(2, 3, 6)
plt.title("alpha = 1.5")
plt.imshow(img)

f_orig = open('C:/Users/akopo/CLionProjects/misoi2/python/histOriginalImage', 'r')
a_orig = []
for line in f_orig:
    a_orig.append([int(x) for x in line.split()])

plt.figure()
plt.hist(a_orig[0], bins=range(0, 256))
plt.title("Original Image")




f_hist1 = open('C:/Users/akopo/CLionProjects/misoi2/python/laplasHFGalpha=1.000000', 'r')
f_hist11 = open('C:/Users/akopo/CLionProjects/misoi2/python/laplasHFGalpha=1.100000', 'r')
f_hist12 = open('C:/Users/akopo/CLionProjects/misoi2/python/laplasHFGalpha=1.200000', 'r')
f_hist13 = open('C:/Users/akopo/CLionProjects/misoi2/python/laplasHFGalpha=1.300000', 'r')
f_hist14 = open('C:/Users/akopo/CLionProjects/misoi2/python/laplasHFGalpha=1.400000', 'r')
f_hist15 = open('C:/Users/akopo/CLionProjects/misoi2/python/laplasHFGalpha=1.500000', 'r')

a_hist1 = []
a_hist11 = []
a_hist12 = []
a_hist13 = []
a_hist14 = []
a_hist15 = []

for line in f_hist1:
    a_hist1.append([int(x) for x in line.split()])
for line in f_hist11:
    a_hist11.append([int(x) for x in line.split()])
for line in f_hist12:
    a_hist12.append([int(x) for x in line.split()])
for line in f_hist13:
    a_hist13.append([int(x) for x in line.split()])
for line in f_hist14:
    a_hist14.append([int(x) for x in line.split()])
for line in f_hist15:
    a_hist15.append([int(x) for x in line.split()])


plt.figure()
plt.subplot(2, 3, 1)
plt.hist(a_hist1[0], bins=range(0, 256))
plt.title("alpha = 1")

plt.subplot(2, 3, 2)
plt.hist(a_hist11[0], bins=range(0, 256))
plt.title("alpha = 1.1")

plt.subplot(2, 3, 3)
plt.hist(a_hist12[0], bins=range(0, 256))
plt.title("alpha = 1.2")

plt.subplot(2, 3, 4)
plt.hist(a_hist13[0], bins=range(0, 256))
plt.title("alpha = 1.3")

plt.subplot(2, 3, 5)
plt.hist(a_hist14[0], bins=range(0, 256))
plt.title("alpha = 1.4")

plt.subplot(2, 3, 6)
plt.hist(a_hist15[0], bins=range(0, 256))
plt.title("alpha = 1.5")

plt.show()