
#Here's how you can define the OCR model:


import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleOCRModel(nn.Module):
    def __init__(self):
        super(SimpleOCRModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output
#```

#This model is a simplified version of a CNN. It has two convolutional layers followed by max-pooling and dropout layers, and finally, two fully connected layers.

#Now, let's integrate this model into your existing code:

import cv2
import torch
import torchvision.transforms as transforms
import tkinter as tk
import numpy as np
from PIL import Image

# Define the OCR model
class SimpleOCRModel(nn.Module):
    def __init__(self):
        super(SimpleOCRModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

# Function to capture image from PC camera
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

# Function to preprocess image
def preprocess_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Resize image to 28x28 (MNIST input size)
    resized = cv2.resize(gray, (28, 28))
    # Normalize pixel values
    normalized = resized / 255.0
    # Convert to PyTorch tensor
    tensor = torch.tensor(normalized, dtype=torch.float).unsqueeze(0).unsqueeze(0)
    return tensor

# Function to handle button click event
def on_enter_click():
    # Capture image
    image = capture_image()
    # Preprocess image
    tensor = preprocess_image(image)
    # Load model
    model = SimpleOCRModel()
    model.load_state_dict(torch.load('mnist_cnn.pth'))  # Load pre-trained weights
    model.eval()
    # Perform inference
    with torch.no_grad():
        output = model(tensor)
    predicted_class = torch.argmax(output).item()
    print("Detected Digit:", predicted_class)

# Create GUI window
root = tk.Tk()
root.title("Handwritten Digit Recognition")

# Create button
button = tk.Button(root, text="Capture Image and Recognize Digit", command=on_enter_click)
button.pack()

# Run GUI loop
root.mainloop()


#This code integrates the OCR model into your existing Tkinter-based GUI application. When you click the button, it captures an image from the PC camera, preprocesses it, performs inference using the OCR model, and prints the recognized digit. Make sure you have a pre-trained model file named `mnist_cnn.pth` in the same directory as your script.