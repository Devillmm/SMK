## To Convert Original Image to Black&White Image by setting Threshold Value
## Original Image --> GrayScale Image --> Setting Threshold Value --> Black&White Image

# Import OpenCV Library
import cv2

# Read the Original Image from Local Directory
Img = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\Basic_Programs\Threshold\Mani.jpg")

# Show / Display the Original Image
cv2.imshow("Original Image",Img)

# To Convert Original Image to Grayscale Image
grayscale = cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

# To Convert GrayScale Image to Black&White Image using Threshold Value
# cv2.threshold(src_Img,Threshold_Value,MaxThresholdValue,Binary_type)[1/0]
ThreshImg = cv2.threshold(grayscale,120,255,cv2.THRESH_BINARY)[1]

# Print Threshold Value
print(ThreshImg) 

# 0 - Black Pixel
# 120 - Threshold Value
# 255 - White Pixel

# Show / Display the Threshold Image
cv2.imshow("Black&White_Image",ThreshImg)

# Write & Save the Threshold Image
cv2.imwrite("C:\\Users\\ADMIN\\Desktop\\SMK\\Python_AI\\AI\\OpenCV\\Basic_Programs\\Threshold\\Output\\Sign.png",ThreshImg)

# Wait Key & Destroy All Windows
cv2.waitKey(5000)

# Destroy All Windows
cv2.destroyAllWindows()
