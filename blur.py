import cv2
img = cv2.imread('gym_4_gray.jpg')

# # resize
# n_width = 900
# n_height = 900
# dim = (n_width, n_height)
# resized_img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

#blur
blur_img = cv2.GaussianBlur(img,(25,25),0)

cv2.imwrite('gym_blur_4.jpg',blur_img)

cv2.imshow('Blur',blur_img)
cv2.waitKey(0)


