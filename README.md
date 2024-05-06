# Camera Text Recognition

This Python script captures an image from the system camera and uses Tesseract OCR to recognize text from the captured image.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`) library
- Tesseract OCR engine
- pytesseract Python wrapper

## Installation

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/).

2. **Install OpenCV**: Install the OpenCV library using pip:
   ```
   pip install opencv-python
   ```

3. **Install Tesseract**: Download and install Tesseract OCR from [GitHub](https://github.com/tesseract-ocr/tesseract). Make sure to add Tesseract to your system PATH.

4. **Install pytesseract**: Install the pytesseract wrapper using pip:
   ```
   pip install pytesseract
   ```

## Usage

1. Clone or download this repository to your local machine.

2. Set the path to the Tesseract executable in the script (`camera_text_recognition.py`) according to your installation:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

3. Run the script:
   ```
   python camera_text_recognition.py
   ```

4. Open your system camera, capture an image, recognize text from the image, and print the recognized text.

 
#DIY
