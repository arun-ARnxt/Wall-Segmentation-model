import cv2

img = cv2.imread('wall_3.jpg')

# resize
n_width = 900
n_height = 900
dim = (n_width, n_height)
resized_img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

img_blur = cv2.GaussianBlur(resized_img,(35,35),0)

ddepth = cv2.CV_16S

grad_x = cv2.Sobel(src=img_blur,ddepth=ddepth,dx=1,dy=0,ksize=3)
grad_y = cv2.Sobel(src=img_blur,ddepth=ddepth,dx=0,dy=1,ksize=3)

abs_grad_x= cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)

grad = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)

cv2.imwrite('Result_edge.jpg',grad)

cv2.imshow('Grad',grad)
cv2.waitKey(0)

