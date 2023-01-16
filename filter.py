import cv2
import numpy as np
import os

def read(path):
    image = cv2.imread(path, 0)
    path_origin = path.replace(".pgm", "") + "_origin"   
    cv2.imshow(path_origin, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # print(type(image))
    return image

def create_kernel(image, i, j, k):
    kernel = np.ones([k,k])
    kernel_i = 0
    for image_i in range(i-k//2, i+k//2+1):
        kernel_j = 0
        for image_j in range(j-k//2, j+k//2+1):
            kernel[kernel_i, kernel_j] = image[image_i, image_j]
            kernel_j += 1
        kernel_i += 1
    return kernel

def averaging_filter(image, path, k=3):
    row, col = image.shape    

    for i in range(k//2, row-k//2):
        for j in range(k//2, col-k//2):
            kernel = create_kernel(image, i, j, k)
            average = kernel.mean()
            image[i,j] = average

    path_new = path.replace(".pgm", "") + "_average_new"   
    cv2.imshow(path_new,image)
    cv2.imwrite("result/" + path_new + ".pgm",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def median_filter(image, path, k=3):
    row, col = image.shape    

    for i in range(k//2, row-k//2):
        for j in range(k//2, col-k//2):
            kernel = create_kernel(image, i, j, k)

            kernel = np.sort(kernel, axis=None)
            # print(kernel)
            median = kernel[(k**2)//2]
            image[i,j] = median    

    path_new = path.replace(".pgm", "") + "_median_new"   
    cv2.imshow(path_new,image)
    cv2.imwrite("result/" + path_new + ".pgm",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

dir_list = os.listdir()
for path in dir_list:
    if not path.find(".pgm") == -1:
        image = read(path)
        averaging_filter(image.copy(), path)
        median_filter(image.copy(), path)

    