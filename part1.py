import cv2
import numpy


def masking(images_list, masks_list, part_info):
    for k in range(0, images_list.__len__()):  # masking the images
        height, width, channels = images_list[k].shape
        for i in range(0, height):
            for j in range(0, width):
                if masks_list[k][i, j] == 0:  # if M(x, y) = 0
                    images_list[k][i, j] = 0  # assign 0
        if part_info == 1:
            cv2.imwrite('part1/masked' + str(k + 1) + '.jpg', images_list[k])  # saving masked images

    return masks_list


def changing_background(images_list, masks_list, background_list, part_info):
    for k in range(0, images_list.__len__()):  # this if for placing to meaningful place.. (it's not mandatory)
        if k == 0:  # knowing which image..
            # this is like hardcoding but
            #  you said "meaningful place" for every image..
            height, width, channels = images_list[k].shape
            masks_list[k] = cv2.resize(masks_list[k], None, fx=0.45, fy=0.45)  # the kid was so big.
            images_list[k] = cv2.resize(images_list[k], None, fx=0.45, fy=0.45)  # So i scale down the image and mask
            m = numpy.float32([[1, 0, 100], [0, 1, 90]])  # 100 pixels right 90 pixels down
            masks_list[k] = cv2.warpAffine(masks_list[k], m, (width, height))  # shifting op
            m = numpy.float32([[1, 0, 100], [0, 1, 90]])  # same operation for mask and image
            images_list[k] = cv2.warpAffine(images_list[k], m, (width, height))
        elif k == 1:
            height, width, channels = images_list[k].shape
            m = numpy.float32([[1, 0, -3], [0, 1, 65]])  # 3 pixels left 65 pixels down
            masks_list[k] = cv2.warpAffine(masks_list[k], m, (width, height))  # shifting op
            m = numpy.float32([[1, 0, -3], [0, 1, 65]])  # same operation for mask and image
            images_list[k] = cv2.warpAffine(images_list[k], m, (width, height))
        elif k == 2:
            height, width, channels = images_list[k].shape
            m = numpy.float32([[1, 0, -40], [0, 1, 50]])  # 40 pixels left 50 pixels down
            masks_list[k] = cv2.warpAffine(masks_list[k], m, (width, height))  # shifting op
            m = numpy.float32([[1, 0, -40], [0, 1, 50]])  # same operation for mask and image
            images_list[k] = cv2.warpAffine(images_list[k], m, (width, height))
        elif k == 3:
            height, width, channels = images_list[k].shape
            masks_list[k] = cv2.resize(masks_list[k], None, fx=0.75, fy=0.75)  # the eagle was so big.
            images_list[k] = cv2.resize(images_list[k], None, fx=0.75, fy=0.75)  # So i scale down the image and mask
            m = numpy.float32([[1, 0, -80], [0, 1, -30]])  # 80 pixels left 30 pixels up
            masks_list[k] = cv2.warpAffine(masks_list[k], m, (width, height))  # shifting op
            m = numpy.float32([[1, 0, -80], [0, 1, -30]])  # same operation for mask and image
            images_list[k] = cv2.warpAffine(images_list[k], m, (width, height))
        elif k == 4:
            height, width, channels = images_list[k].shape
            m = numpy.float32([[1, 0, -20], [0, 1, 50]])  # 20 pixels left 50 pixels down
            masks_list[k] = cv2.warpAffine(masks_list[k], m, (width, height))  # shifting op
            m = numpy.float32([[1, 0, -20], [0, 1, 50]])  # same operation for mask and image
            images_list[k] = cv2.warpAffine(images_list[k], m, (width, height))

    for k in range(0, background_list.__len__()):
        height, width, channels = background_list[k].shape  # taking width and height values
        for i in range(0, height):
            for j in range(0, width):
                if masks_list[k][i, j] != 0:  # if mask image's current pixel is not zero(black)
                    background_list[k][i, j] = images_list[k][i, j]  # then write the foreground object on background
        if part_info == 1:
            cv2.imwrite('part1/changed' + str(k + 1) + '.jpg', background_list[k])  # saving final phase of the images
        if part_info == 2:
            cv2.imwrite('part2/changed' + str(k + 1) + '.jpg', background_list[k])  # saving final phase of the images

