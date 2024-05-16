import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Function to extract and preprocess plate number from an image
def extract_plate_number(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 10)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for contour in contours:
        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Apply OCR to the preprocessed image
    plate_text = pytesseract.image_to_string(image)

    # Use regular expression to find the plate number pattern
    plate_number = re.search(r'[A-Z]{3}\d{4}', plate_text)
    if plate_number:
        return plate_number.group().upper()  # Return the match found and convert to uppercase
    else:
        return None  # Return None if no plate number is found


# Function to compare extracted plate number with stored plate number
def compare_plate_numbers(extracted_plate_number, stored_plate_number):
    if extracted_plate_number == stored_plate_number:
        return True
    else:
        return False


# Example usage
stored_plate_number = "ABC1234"  # Example stored plate number
image_path ='C:/Users/ENGR. ISRAEL/Documents/Python Scripts/e.png'  # Example path to the image containing the license plate

extracted_plate_number = extract_plate_number(image_path)

if extracted_plate_number:
    print("Extracted plate number:", extracted_plate_number)
    if compare_plate_numbers(extracted_plate_number, stored_plate_number):
        print("Plate numbers match!")
    else:
        print("Plate numbers do not match.")
else:
    print("No plate number found in the image.")
