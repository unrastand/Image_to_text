# License Plate Recognition System

This project is a license plate recognition system that captures an image of a vehicle's license plate using a camera, processes the image to recognize the text on the plate, and checks it against a database of authorized license plates. If the license plate is found in the database, the system sends a signal to open a gate.

## Features

- Captures image of the license plate using a webcam.
- Processes the image to extract the license plate region.
- Recognizes text from the license plate using Tesseract OCR.
- Compares the recognized text with a database of authorized license plates.
- Sends a signal to an Arduino to control a gate motor if the license plate is authorized.

## Requirements

- Python 3.x
- OpenCV
- Tesseract OCR
- PySerial
- Difflib
- License database (custom module)

## Installation

1. Install Python 3.x from the official website: https://www.python.org/

2. Install required Python packages using pip:
   ```bash
   pip install opencv-python pytesseract pyserial
   ```

3. Install Tesseract OCR from: https://github.com/tesseract-ocr/tesseract

4. Set the path to the Tesseract executable in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

5. Connect the Arduino to your computer and set the correct serial port in the script:
   ```python
   serial_port = 'COM3'  # Update with your Arduino Nano's serial port
   ```

## Usage

1. Ensure that your Arduino is connected and properly configured to control the gate motor.

2. Run the Python script:
   ```bash
   python license_plate_recognition.py
   ```

3. The system will wait for data from the Arduino to start the video capture. Once it receives the signal, it will start capturing video from the webcam.

4. The script processes each frame to detect and recognize the license plate. If the plate is recognized and authorized, it sends a signal to the Arduino to open the gate.

## Code Overview

- **main.py**: Main script that captures video, processes the image, recognizes text, and controls the gate.
- **crop_black_quadrilateral**: Function to detect and crop the rectangular region containing the license plate.
- **recognize_text**: Function to recognize text from the cropped license plate image using Tesseract OCR.
- **most_similar_license**: Function to find the most similar license plate in the database.
- **send_data**: Function to send data to the Arduino to control the gate motor.
 

## Acknowledgements

- Tesseract OCR: https://github.com/tesseract-ocr/tesseract
- OpenCV: https://opencv.org/
- PySerial: https://pyserial.readthedocs.io/en/latest/

## Contact

For any questions or issues, please contact [Your Name] at [Your Email].