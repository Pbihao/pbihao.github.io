import cv2

img = cv2.imread("ph.png")
cv2.imwrite("2024CVPR_PromptHilighter.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 85])