import cv2
import pytesseract

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to capture image from PC camera
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

# Function to convert image to text using Tesseract OCR
def image_to_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Main function
def main():
    while True:
        # Capture image from PC camera
        image = capture_image()

        # Convert image to text
        text = image_to_text(image)

        # Print detected text
        print("Detected Text:")
        print(text)

        # Display the captured image
        cv2.imshow('Captured Image', image)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
