import cv2
import pytesseract
import serial #install pyserial library
import time

# Set the path to Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#list of saved license plates

allowed_plates = ["ABS-234","23S-DAF"]

# Serial port configuration
serial_port = '/dev/ttyUSB0'  # Update this with your Arduino Nano's serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)
time.sleep(2) #wait fir arduino to initialize

# Function to send command to Arduino Nano to control motors
def send_command(command):
    ser.write(command.encode())

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


# Function to receive data from Arduino Nano
def receive_data():
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        return data
    else:
        return None


# Function to send data to Arduino Nano to control motors
def send_data(data):
    ser.write(data.encode())



# Main function
def main():

    # Capture image from camera
    image = capture_image()

    # Check if image capture was successful
    if image is not None:
        # Recognize text from the captured image
        text = recognize_text(image)

        #check to open and close the gate 
        for a in allowed_plates:
            if text == a:
                send_data("open")
            

        # Print the recognized text 
        # please confirm what it prints from camera and saved to allowed_plates list
        print("Recognized Text:")
        print(text)
    else:
        print("Error: Failed to capture image.")

if __name__ == "__main__":
    while True:
        # 1 means data from arduino to start process

        if receive_data() == 1:
            main()
        
