## To Convert Original Image to Grayscale Image using OpenCV Library

# Import OpenCV Library
import cv2

# Read the Image from Local Directory
O_Img = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\Basic_Programs\GrayScale\ironman.jpg")

# Show / Display the Original Image
cv2.imshow("Original Image",O_Img)

# Convert to Grayscale Image
grayscale = cv2.cvtColor(O_Img,cv2.COLOR_BGR2GRAY)

# Show / Display the Grayscale Image
cv2.imshow("Grayscale Image",grayscale)

# Write & Save the Grayscale Image
cv2.imwrite("C:\\Users\\ADMIN\\Desktop\\SMK\\Python_AI\\AI\\OpenCV\\Basic_Programs\\GrayScale\\Output\\Mark42.jpeg",grayscale)

# Wait Key - Key to Exit from Output
cv2.waitKey(10000)

# Destroy All Windows
cv2.destroyAllWindows()