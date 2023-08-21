import cv2
import numpy as np

def detect_changes(old_image_path, new_image_path, save_path="results/detected_changes.png"):
    # Load the images in grayscale
    old_image = cv2.imread(old_image_path, cv2.IMREAD_GRAYSCALE)
    new_image = cv2.imread(new_image_path, cv2.IMREAD_GRAYSCALE)

    # Compute the absolute difference between the two images
    difference = cv2.absdiff(old_image, new_image)

    # Threshold the difference image
    _, thresholded = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    # Find contours of the changes
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around changes on the new image
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(new_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the result
    cv2.imwrite(save_path, new_image)

    return save_path
