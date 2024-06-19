import cv2

img = cv2.imread("thumbnails.png")
cv2.imwrite("2024CVPR_GroupContrast.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 85])