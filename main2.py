import cv2
from openocr import OCR
import tkinter as tk

# Function to capture image from PC camera
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

# Function to convert image to text using OpenOCR
def image_to_text(image):
    ocr = OCR()
    text = ocr.ocr_image(image)
    return text

# Function to handle button click event
def on_enter_click():
    image = capture_image()
    text = image_to_text(image)
    print("Detected Text:")
    print(text)

# Create GUI window
root = tk.Tk()
root.title("Capture and Convert Image to Text")

# Create button
button = tk.Button(root, text="Capture Image and Convert to Text", command=on_enter_click)
button.pack()

# Run GUI loop
root.mainloop()
