from src.change_detection import detect_changes
from src.ocr_extraction import extract_text_from_image

def main():
    old_diagram_path = "data/old_diagrams/sample_old.png"
    new_diagram_path = "data/new_diagrams/sample_new.png"

    result_image_path = detect_changes(old_diagram_path, new_diagram_path)

    text = extract_text_from_image(result_image_path)
    print(text)

if __name__ == '__main__':
    main()
