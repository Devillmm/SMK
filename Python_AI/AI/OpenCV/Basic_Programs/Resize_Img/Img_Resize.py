## To Resize an Image using IMUTILS Library

# Import OpenCV Library
import cv2

# Import Imutils Library
import imutils

# Read the Image from Local Directory
Img = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\Basic_Programs\Resize_Img\SMK2.png")

# Show / Display the Image
cv2.imshow("Original_Image",Img)

# Resize the Original Image using Imutils
Resize = imutils.resize(Img,width=500)

# Show / Display the Resized Image
cv2.imshow("Resized Image",Resize)

# Write & Save the Resized Image
cv2.imwrite("C:\\Users\\ADMIN\\Desktop\\SMK\\Python_AI\\AI\\OpenCV\\Basic_Programs\\Resize_Img\\Output\\Resized.jpg",Resize)

# WaitKey & Destroy All Windows
cv2.waitKey(5000)
cv2.destroyAllWindows()
