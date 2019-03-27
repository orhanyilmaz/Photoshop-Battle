import cv2
import numpy
import math
import glob


def blurring(sigma):
    backgrounds_list = []
    size = (sigma * 2 * 2) + 1
    blurred_list = []
    sqr2pi = math.sqrt(2 * math.pi)
    width = int(size / 2) or 0
    kernel1d = [None]*(width * 2 + 1)
    norm = 1.0 / (sqr2pi * sigma)
    coefficient = 2 * sigma * sigma
    total = 0

    for filename in sorted(glob.glob('images/background*.jpg')):
        im = cv2.imread(filename)
        backgrounds_list.append(im)

    for x in range(-width, width+1):
        kernel1d[width + x] = norm * math.exp(-x * x / coefficient)
        total += kernel1d[width + x]

    for x in range(0, len(kernel1d)):
        kernel1d[x] /= total

    vertical_one = numpy.reshape(kernel1d, (1, size))  # list to array
    kernel2d = numpy.matmul(numpy.vstack(kernel1d), vertical_one)  # 1d to 2d (transpose and matrix multiplication)

    for i in range(0, backgrounds_list.__len__()):
        blurred_list.append(cv2.filter2D(backgrounds_list[i], cv2.CV_64F, kernel2d, anchor=(-1, -1), borderType=cv2.BORDER_REFLECT_101))
        cv2.imwrite('part2/blurred' + str(i + 1) + '.jpg', blurred_list[i])  # saving final phase of the images

    return kernel2d, blurred_list


def sharpening(kernel2d, alpha):
    unsharpen_list = []
    images_list = []
    for filename in sorted(glob.glob('part1/masked*.jpg')):
        im2 = cv2.imread(filename)
        images_list.append(im2)

    for i in range(0, images_list.__len__()):
        blurred = cv2.filter2D(images_list[i], cv2.CV_64F, kernel2d, anchor=(-1, -1), borderType=cv2.BORDER_REFLECT_101)
        diff_images = numpy.subtract(images_list[i], blurred)
        unsharpen_list.append(cv2.add(images_list[i].astype(float), (alpha * diff_images.astype(float))))
        cv2.imwrite('part2/sharpened_foreground' + str(i + 1) + '.jpg', unsharpen_list[i])  # sharp_foreground images

    return unsharpen_list
