## To Find the Absolute Difference of the Given Images
# Syntax: cv2.absdiff(srcImg1,srcImg2)

#Import OpenCV Library
import cv2

# Read the Image 1 & Image 2
Img1 = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\Basic_Programs\Absolute_Difference\Absdiff_1\Image_1.jpg")
Img2 = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\Basic_Programs\Absolute_Difference\Absdiff_1\Image_2.jpg")

# Print the Image Size of Both Images
print("Image 1 Size: ",Img1.size)
print("Image 2 Size: ",Img2.size)

# Print the Image Shape of Both Images
print("Image 1 Shape: ",Img1.shape)
print("Image 2 Shape: ",Img2.shape)

# Find Absolute Difference
absdif = cv2.absdiff(Img1,Img2)

# Convert to GrayScale Image
grayscale = cv2.cvtColor(absdif,cv2.COLOR_BGR2GRAY)

# Convert GrayScale Image to Black&White Image
threshImg = cv2.threshold(grayscale,25,255,cv2.THRESH_BINARY)[1]

# Show / Display the AbsDiff Image
cv2.imshow("Absolute Difference Image",absdif)

# Show / Display the Threshold Image
cv2.imshow("Threshold Image",threshImg)

# Save the Absolute Difference Image
cv2.imwrite("C:\\Users\\ADMIN\\Desktop\\SMK\\Python_AI\\AI\\OpenCV\\Basic_Programs\\Absolute_Difference\\Absdiff_1\\Absdiff_Final_1.png",absdif)

# Save the Threshold Image\
cv2.imwrite("C:\\Users\\ADMIN\\Desktop\\SMK\\Python_AI\\AI\\OpenCV\\Basic_Programs\\Absolute_Difference\\Absdiff_1\\Absdiff_Thresh_2.png",threshImg)

# Key to Exit from Output
cv2.waitKey(5000)

# Destroy All Windows
cv2.destroyAllWindows()