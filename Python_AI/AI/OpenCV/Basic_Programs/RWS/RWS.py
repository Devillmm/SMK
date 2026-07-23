## To Access the Image from Local Directory using OpenCV Library

# Import OpenCV Library
import cv2

# Read the Image from Local Directory
Img = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\Basic_Programs\RWS\hulk.jpg")

# Show / Display the Image
cv2.imshow("HULK",Img)

# Write & Save the Image (Format Change)
cv2.imwrite("Basic_programs\RWS\Output\Smash.png", Img)

# Wait Key - Key to Exit from Output (in ms)
cv2.waitKey(5000) #5 seconds

# Destroy All Windows
cv2.destroyAllWindows()

