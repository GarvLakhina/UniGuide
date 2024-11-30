from PIL import Image
import pytesseract

def process_image(image_path):
    # Convert image to text using OCR
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    
    return f"Extracted text from image: {text}"
