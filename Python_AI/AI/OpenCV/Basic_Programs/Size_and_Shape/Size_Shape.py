## Print the Size & Shape of an Image

# Import OpenCV Library
import cv2

# Read the Image from Local Directory 
Img = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\Basic_Programs\Size&Shape\DP.jpeg")

# Show / Display the Image
cv2.imshow("Original Image",Img)

# Write & Save the Image
cv2.imwrite("Basic_Programs\Size&Shape\Lucifer.png",Img)

# Wait Key 
cv2.waitKey(5000) # 5seconds

# Destroy All Windows
cv2.destroyAllWindows()

# Print Image Size
print("Image Size: ",Img.size)
# Out - 3499200

# Print Image Shape
print("Image Shape: ",Img.shape)
# Out - (1080,1080,3) - (H,W,BGR)