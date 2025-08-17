import cv2
from util import get_limits

cap = cv2.VideoCapture(0) # Open the default camera
blue = [255, 0, 0]  # Define a blue color in BGR format

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame to HSV color space
    lower_limit, upper_limit = get_limits(blue)  # Get the HSV limits for the defined color
    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)  # Create a mask for the defined color
    
    cv2.imshow('frame', frame)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows