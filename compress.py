import cv2

img = cv2.imread("2024CVPR_OACNN.png")
cv2.imwrite("2024CVPR_OACNN.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 85])