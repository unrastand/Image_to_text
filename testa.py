import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
states={
    "AN": "Andaman"
}
def extract_num(imag_name):
    global read
    img = cv2.imread(imag_name)
    # Get the dimensions of the image
    height, width, channels = img.shape

    # Print the dimensions
    print("Width:", width)
    print("Height:", height)
    print("Channels:", channels)

    # Calculate the scale factor based on the image height
    scale_factor = min(1.1, 1000 / 2)#img_height)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    nplate = cascade.detectMultiScale(gray)
    for (x,y,w,h) in nplate:
        a,b = (int(0.02*img.shape[0]), int(0.025*img.shape[1]))
        plate = img[y+a:y+h-a, x+b:x+w-b,:]
        kernel = np.ones((1,1), np.uint8)
        plate = cv2.dilate(plate, kernel, iterations=1)
        plate = cv2.erode(plate, kernel, iterations=1)
        plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        _, plate = cv2.threshold(plate_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Detected License Plates', plate )
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        read = pytesseract.image_to_string(plate)
        print("License Plate Number:", read)

# Call the function with the image file name and height
image_height = 102  # Example height of the image
extract_num('th.jfif')#, image_height)
