import cv2
import pytesseract

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to read image from file
def read_image(file_path):
    image = cv2.imread(file_path)
    return image

# Function to convert image to text using Tesseract OCR
def image_to_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Main function
def main():
    # Path to the image file
    image_path = 'C:/Users/ENGR. ISRAEL/Documents/Python Scripts/a.jfif'

    # Read image from file
    image = read_image(image_path)

    # Convert image to text
    text = image_to_text(image)

    # Print detected text
    print("Detected Text:")
    print(text)

if __name__ == "__main__":
    main()
