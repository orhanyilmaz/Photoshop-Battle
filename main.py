import os
import part1
import part2
import glob
import cv2

masks_list = []
masks2_list = []
images_list = []
background_list = []

try:  # creating part1,2 folders
    if not os.path.exists('./part1/'):
        os.makedirs('./part1/')
    if not os.path.exists('./part2/'):
        os.makedirs('./part2/')
except OSError:
    print('Error')

for filename in sorted(glob.glob('images/mask*.png')):  # reading images and masks from disk
    im = cv2.imread(filename, 0)
    masks_list.append(im)  # adding to list
    masks2_list.append(im)  # add this prevent the finding meaningful place process works 2 times

for filename in sorted(glob.glob('images/im*.jpg')):
    im = cv2.imread(filename)
    images_list.append(im)


for filename in sorted(glob.glob('images/background*.jpg')):
    im = cv2.imread(filename)
    background_list.append(im)

# running all functions in here

# this section for part1


part1.masking(images_list, masks_list, 1)  # this is masking (part1.1)

part1.changing_background(images_list, masks2_list, background_list, 1)  # this is changing background (part1.2)


# this section for part2

kernel2d, blurred_list = part2.blurring(1)  # this is blurring background (part2.1)

unsharpen_list = part2.sharpening(kernel2d, 0.4)  # this is sharpening foreground (part2.2)


# this section for the same steps part1 for part2


part1.changing_background(unsharpen_list, masks_list, blurred_list, 2)  # this is changing background
