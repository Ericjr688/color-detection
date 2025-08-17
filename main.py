import cv2
from util import get_limits
from PIL import Image

color_map = {
    "blue": [255, 0, 0],
    "red": [0, 0, 255],
    "yellow": [0, 255, 255],
    "purple": [128, 0, 128]
}

print("Available colors: ", ", ".join(color_map.keys()))
selected_color = input("Enter a color from the list: ").strip().lower()

if selected_color not in color_map:
    print("Invalid color selected. Exiting...")
    exit()

# Get the BGR value of the selected color
bgr_color = color_map[selected_color]

cap = cv2.VideoCapture(0)  # Open the default camera

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame to HSV color space
    lower_limit, upper_limit = get_limits(bgr_color)  # Get the HSV limits for the selected color
    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)  # Create a mask for the selected color

    mask_ = Image.fromarray(mask)  # Convert the mask to a PIL Image for further processing if needed
    bbox = mask_.getbbox()  # Get the bounding box of the non-zero regions in the mask

    if bbox:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)  # Draw a rectangle around the detected color
    
    cv2.imshow('frame', frame)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows