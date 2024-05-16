import cv2
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Function to capture image from system camera
def capture_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    return image


# Function to recognize text from the captured image
def recognize_text(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter to smooth the image while preserving edges
    smoothed_image = cv2.bilateralFilter(gray_image, 11, 17, 17)

    # Apply Canny edge detection
    edged = cv2.Canny(smoothed_image, 30, 200)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area and keep only the largest ones
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    # Draw contours on the image (for debugging)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    # Iterate over the contours
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Extract the region of interest (ROI) containing the text
        roi = image[y:y + h, x:x + w]

        # Apply OCR to the ROI
        text = pytesseract.image_to_string(roi)

        # Print the recognized text
        print("Recognized Text:", text.strip())

    # Display the processed image (for debugging)



# Main function
def main():
    # Capture image from camera
    image_path = 'C:/Users/ENGR. ISRAEL/Downloads/license-plate-main/license-plate-main/62.png'
    image = capture_image(image_path)

    # Recognize text from the captured image
    recognize_text(image)


if __name__ == "__main__":
    main()
