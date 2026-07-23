## Smoothening the Image using Gaussian Blur

# Import OpenCV Library
import cv2

# Read the Image from Local Directory
Img = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\Basic_Programs\Smoothening(GB)\SMK2.png")

# Show / Display the Original Image
cv2.imshow("Original_Image",Img)

# Gaussian Blur - Smoothening
# GaussianBlur = cv2.GaussianBlur(src_Img,(Kernal),border_type)
gblr = cv2.GaussianBlur(Img,(21,21),1)

# kernal = (41,41)
# gblr1 = cv2.GaussianBlur(Img,(41,41),1)

# Show / Display the Gaussian Blur Image
cv2.imshow("GaussianBlur_Image1",gblr)

# cv2.imshow("GaussianBlur_Image2",gblr1)

# Write & Save the Gaussian Blur Image
cv2.imwrite("Basic_Programs\Smoothening(GB)\Output\Smoothened_SMK.jpeg",gblr)

# Wait Key
cv2.waitKey(10000)

# Destroy All Windows
cv2.destroyAllWindows()

