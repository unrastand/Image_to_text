import cv2
import pytesseract

# Set the path to Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to capture image from system camera
def capture_image():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened correctly
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    return frame

# Function to recognize text from the captured image
def recognize_text(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract OCR to recognize text from the image
    text = pytesseract.image_to_string(gray_image)

    return text

# Main function
def main():
    # Capture image from camera
    image = capture_image()

    # Check if image capture was successful
    if image is not None:
        # Recognize text from the captured image
        text = recognize_text(image)

        # Print the recognized text
        print("Recognized Text:")
        print(text)
    else:
        print("Error: Failed to capture image.")

if __name__ == "__main__":
    main()
