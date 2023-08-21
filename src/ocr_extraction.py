import cv2
from pytesseract import image_to_string

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    extracted_text = image_to_string(rgb_image)
    return extracted_text
