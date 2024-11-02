import cv2
import os
import numpy as np

number_of_images = 486

for i in range(486):
    img = cv2.imread(os.path.join("images", "image_" + str(i) + ".jpg"))
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    LOWER = np.array([40,30,80]) # for outdoor
    UPPER = np.array([100,255,255])

    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Apply mask to isolate the green areas
    mask = cv2.inRange(hsv_image, LOWER, UPPER)
    green_areas = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
    inverted_mask = cv2.bitwise_not(mask)
    non_green_areas = cv2.bitwise_and(hsv_image, hsv_image, mask=inverted_mask)

    non_green_areas[:, :, 2] = non_green_areas[:, :, 2] * 0.5
    final_img = cv2.cvtColor(non_green_areas, cv2.COLOR_HSV2RGB)
    final_img = final_img + cv2.cvtColor(green_areas, cv2.COLOR_HSV2BGR)
    gray_img = cv2.cvtColor(final_img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(os.path.join("images_bw", "image_" + str(i) + ".jpg"), gray_img)