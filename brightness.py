import cv2

image=cv2.imread('All_images/wall.jpg')

# resize
# n_width = 600
# n_height = 600
# dim = (n_width, n_height)
# resized_new = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)

# convert to gray scale image
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# brightness change
alpha = 1
beta =  100
new_image = cv2.convertScaleAbs(gray_image,alpha=alpha, beta=beta)

cv2.imwrite('gray_results/gray_95.jpg',new_image)
cv2.imshow('Image',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()