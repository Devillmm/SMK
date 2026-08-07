### FACE DETECTION MODEL BY USING AN IMAGE

# Import OpenCV Library
import cv2

# Loading Haar Cascade FrontalFace Algorithm
haar_alg = "C:\\Users\\ADMIN\\Desktop\\SMK\\Python_AI\\AI\\OpenCV\\AI_OPENCV_PROJECTS\\P2_Face_Detection_Model\\haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(haar_alg)
print("Algorithm Loaded Successfully: ",haar_cascade)

# Read the Image
Load_img = cv2.imread(r"C:\Users\ADMIN\Desktop\SMK\Python_AI\AI\OpenCV\AI_OPENCV_PROJECTS\P2_Face_Detection_Model\Face_Detection_Model_Using_Image\crowd_2.png")

# Display the Original Image
# cv2.imshow("Original",Load_img)

# Convert to GRAYSCALE Image
grayscale = cv2.cvtColor(Load_img,cv2.COLOR_BGR2GRAY)

# Obtaining Face Co-ordinates by passing Algorithms
# --- Mantatory to pass GRAYSCALE Image ---
img_faces = haar_cascade.detectMultiScale(grayscale,1.1,6)

# Draw the Rectangle Bounding Box for each Faces
for (x,y,w,h) in img_faces:
    cv2.rectangle(Load_img,(x,y),(x+w,y+h),(0,0,255),3)
print("FACE DETECTED: ",len(img_faces))

# Display the Face Detection using Image Output
cv2.imshow("FACE DETECTION IN IMAGE",Load_img)

# Key to Exit from Output
cv2.waitKey(10000)

# Destroy All Windows
cv2.destroyAllWindows()