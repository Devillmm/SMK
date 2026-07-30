## Live Video Streaming using OpenCV

# Import OpenCV & Imutils
import cv2
import imutils

# Initializing Camera ID
live_vs = cv2.VideoCapture(0)

# (0) - Primary Camera ID
# (1) - Secondary Camera ID

while True:     # Infinite Loop
    # Read the Frames from Camera
    camcheck,Live_Stream = live_vs.read()
    print("Camera Detected: ",camcheck) #True

    # Resize the Camera Frame
    Live_Stream= imutils.resize(Live_Stream,width=500)
    
    # Show / Display the Live Video Stream
    cv2.imshow("LIVE",Live_Stream)

    # Key to Exit from Live Stream
    Key = cv2.waitKey(1) & 0xFF
    print("WaitKey: ",Key) #255
    if Key == ord("E"): #"E" = 69 [Exit]
        break

# Release Camera ID     
live_vs.release()

# Destroy All Windows
cv2.destroyAllWindows()


