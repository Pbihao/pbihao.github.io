import cv2

img = cv2.imread("2023CVPR_HDMNet.png")
cv2.imwrite("2023CVPR_HDMNet.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 85])