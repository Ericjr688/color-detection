import cv2

cap = cv2.VideoCapture(0) # Open the default camera

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    cv2.imshow('frame', frame)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows