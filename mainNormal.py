import cv2
import pytesseract
import serial  # install pyserial library
import time
from difflib import SequenceMatcher
import license_database

# Set the path to Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Serial port configuration
serial_port = 'COM3'  # Update this with your Arduino Nano's serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)
time.sleep(2)  # wait for arduino to initialize


# to check how well the plate numbers match ones in the database
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def most_similar_license(License):
    most_similar = None
    high_score = 0
    for l in license_database.read_license():
        score = similar(l[0], License)
        if score > high_score:
            high_score = score
            most_similar = l[0]
    if most_similar is None or high_score < 0.7:
        return None
    return most_similar


def check_image(img):
    cropped_img = crop_black_quadrilateral(img)
    # checks if image exists or contain any value
    if cropped_img is not None and cropped_img.any():
        try:
            license_text = get_text(cropped_img).upper()
            license_database_text = most_similar_license(license_text)
            if license_database_text is None and len(license_text) > 5:
                print(f"Could not find {license_text} license plate in license_database")
            else:
                print("The license plate was found as: " + license_database_text)
                print("open")
                # sends data to open the gate
                send_data("open")
                return "quit"
        except Exception as e:
            print(f"Error: {e}")
            pass
    return None


# Function to recognize text from the captured image
def recognize_text(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract OCR to recognize text from the image
    text = pytesseract.image_to_string(gray_image,
                                       config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8',
                                       lang='eng')

    return text.strip()


# Function to receive data from Arduino Nano
def receive_data():
    if ser.in_waiting > 0:
        data = ser.readline().decode()
        return data

    return None


# Function to send data to Arduino Nano to control motors
def send_data(data):
    ser.write(data.encode())


def crop_black_quadrilateral(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)

    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(c)
            new_img = img[y:y + h, x:x + w]
            return new_img

    return None


def get_text(image):
    value = pytesseract.image_to_string(image,
                                        config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8',
                                        lang='eng')

    def charToNumber(char: str):
        char_dict = {
            "0": "O",
            "1": "I",
            "3": "B",
            "4": "A",
            "5": "S",
            "6": "G",
            "7": "Z",
            "8": "B",
        }
        return char_dict.get(char, char)

    if len(value) < 4:
        raise Exception("Could not generate a valid plate number")
    if len(set(value) & set("0123456789")) == 0:
        return ""
    value = value.strip()
    return charToNumber(value[0]) + charToNumber(value[1]) + value[2:-2] + charToNumber(value[-2]) + charToNumber(
        value[-1])


if __name__ == "__main__":
    while True:
        print("Waiting for data from Arduino...")
        data = receive_data()
        print(f"Received data: {data}")

        if data:
            print("Starting video capture...")
            video = cv2.VideoCapture(0)
            if not video.isOpened():
                print("Failed to open video capture")
                continue
            while video.isOpened():
                ret, frame = video.read()
                if frame is None:
                    print("No frame captured")
                    continue
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('Frame', gray)
                value = pytesseract.image_to_string(gray,
                                                    config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8',
                                                    lang='eng')
                c = check_image(frame)
                if (cv2.waitKey(1) == ord("q")) or c == "quit":
                    video.release()
                    cv2.destroyAllWindows()
                    break
            video.release()
            ser.close()
            print("Video capture ended")
        else:
            print("No valid data received or data not equal to '1'")
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage
        if not ser.is_open:
            ser.open()
