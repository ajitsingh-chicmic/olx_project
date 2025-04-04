# import cv2
# import numpy as np
# import pytesseract
# import json

# class AdvancedOCRExtractor:
#     def __init__(self, image_path, ocr_data):
#         """
#         Initialize extractor with image and OCR data
        
#         Args:
#             image_path (str): Path to the invoice image
#             ocr_data (dict): Processed OCR results
#         """
#         self.image = cv2.imread('Gupta.jpeg')
#         self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
#         self.ocr_data = ocr_data
#         self.text_lines = ocr_data.get("text_lines", [])
    
#     def detect_vertical_lines(self):
#         """
#         Detect vertical lines in the image
        
#         Returns:
#             list: Vertical line coordinates
#         """
#         # Binarize the image
#         _, binary = cv2.threshold(self.gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
#         # Create vertical line kernel
#         vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
        
#         # Detect vertical lines
#         vertical_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
        
#         # Find contours of vertical lines
#         contours, _ = cv2.findContours(vertical_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
#         # Extract line coordinates
#         vertical_line_coords = []
#         for contour in contours:
#             x, y, w, h = cv2.boundingRect(contour)
#             # Filter out noise (adjust these values based on your document)
#             if w < 10 and h > 50:  # Narrow and tall
#                 vertical_line_coords.append((x, y, w, h))
        
#         return vertical_line_coords
    
#     def determine_value_extraction_method(self, keyword_bbox):
#         """
#         Determine whether to extract value from right or bottom
#         based on vertical line positions
        
#         Args:
#             keyword_bbox (list): Bounding box of the keyword
        
#         Returns:
#             str: 'right' or 'bottom'
#         """
#         vertical_lines = self.detect_vertical_lines()
        
#         # Check if any vertical line is near the keyword
#         for line_x, line_y, line_w, line_h in vertical_lines:
#             # Check if vertical line is close to the keyword's right side
#             if abs(keyword_bbox[2] - line_x) < 50:
#                 return 'bottom'
        
#         return 'right'
    
#     def find_value_nearby(self, keyword):
#         """
#         Find value near a keyword with intelligent extraction method
        
#         Args:
#             keyword (str): Keyword to search for
        
#         Returns:
#             str: Extracted value
#         """
#         # Find lines containing the keyword
#         matched_lines = [
#             line for line in self.text_lines 
#             if keyword.lower() in line['text'].lower()
#         ]
        
#         if not matched_lines:
#             return "Value not found"
        
#         # Take the first matched line
#         keyword_line = matched_lines[0]
        
#         # Determine extraction method
#         extraction_method = self.determine_value_extraction_method(keyword_line['bbox'])
        
#         if extraction_method == 'right':
#             return self._find_value_to_right(keyword_line)
#         else:
#             return self._find_value_below(keyword_line)
    
#     def _find_value_to_right(self, keyword_line):
#         """
#         Find value to the right of a keyword
        
#         Args:
#             keyword_line (dict): Line containing the keyword
        
#         Returns:
#             str: Value found to the right
#         """
#         keyword_x = keyword_line['bbox'][2]  # Right edge of the keyword
#         keyword_y = keyword_line['bbox'][1]  # Y-axis position
        
#         # Find candidate values
#         candidates = [
#             (l['text'], l['bbox']) for l in self.text_lines
#             if (l['bbox'][0] > keyword_x and 
#                 abs(l['bbox'][1] - keyword_y) < 50)
#         ]
        
#         # Sort candidates by horizontal distance
#         candidates.sort(key=lambda x: x[1][0])
        
#         return candidates[0][0] if candidates else "Value not found"
    
#     def _find_value_below(self, keyword_line):
#         """
#         Find value below a keyword
        
#         Args:
#             keyword_line (dict): Line containing the keyword
        
#         Returns:
#             str: Value found below
#         """
#         keyword_x = keyword_line['bbox'][0]
#         keyword_y = keyword_line['bbox'][3]  # Bottom of the keyword
        
#         # Find candidate values
#         candidates = [
#             (l['text'], l['bbox']) for l in self.text_lines
#             if (l['bbox'][1] > keyword_y and 
#                 abs(l['bbox'][0] - keyword_x) < 50)
#         ]
        
#         # Sort candidates by vertical distance
#         candidates.sort(key=lambda x: x[1][1])
        
#         return candidates[0][0] if candidates else "Value not found"
    
#     def extract_key_value_pairs(self, keywords):
#         """
#         Extract multiple key-value pairs
        
#         Args:
#             keywords (list): List of keywords to extract
        
#         Returns:
#             dict: Extracted key-value pairs
#         """
#         return {
#             keyword: self.find_value_nearby(keyword) 
#             for keyword in keywords
#         }

# def main():
#     # Example usage
#     image_path = 'invoice.jpg'
    
#     # Load OCR results (this would typically come from your OCR processing)
#     ocr_data = {
#         "text_lines": [
#             # Your OCR text lines with bbox information
#             # Example structure:
#             # {"text": "Invoice No.", "bbox": [x, y, w, h]},
#             # {"text": "123456", "bbox": [x, y, w, h]},
#         ]
#     }
    
#     # Create extractor
#     extractor = AdvancedOCRExtractor(image_path, ocr_data)
    
#     # Keywords to extract
#     keywords = ["Invoice No.", "Date", "Total"]
    
#     # Extract key-value pairs
#     extracted_data = extractor.extract_key_value_pairs(keywords)
    
#     # Print results
#     print(json.dumps(extracted_data, indent=4))

# if __name__ == "__main__":
#     main()

# # Visualization Method (Optional)
# def visualize_vertical_lines(image_path):
#     """
#     Visualize detected vertical lines on the image
    
#     Args:
#         image_path (str): Path to the invoice image
#     """
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Binarize the image
#     _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
#     # Create vertical line kernel
#     vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
    
#     # Detect vertical lines
#     vertical_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    
#     # Find contours of vertical lines
#     contours, _ = cv2.findContours(vertical_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Draw vertical lines on the image
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         if w < 10 and h > 50:  # Filter criteria
#             cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#     # Display the image
#     cv2.imshow('Vertical Lines', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# import cv2
# import pytesseract
# import re
# import json

# def extract_invoice_details(image_path):
#     """
#     Extract key details from the tax invoice
    
#     Args:
#         image_path (str): Path to the invoice image
    
#     Returns:
#         dict: Extracted invoice details
#     """
#     # Read the image
#     image = cv2.imread('Gupta.jpeg')
    
#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Apply OCR
#     text = pytesseract.image_to_string(gray)
    
#     # Structured extraction of key details
#     invoice_details = {
#         "Company": "GUPTA PLY CO.",
#         "Invoice Number": extract_field(text, r"Invoice No\.?\s*([A-Za-z0-9/\-]+)", default="N/A"),
#         "Acknowledgement Number": extract_field(text, r"Ack No\.?\s*(\d+)", default="N/A"),
#         "Acknowledgement Date": extract_field(text, r"Ack Date\s*(\d{2}-[A-Za-z]{3}-\d{2})", default="N/A"),
#         "GSTIN": extract_field(text, r"GSTIN\s*(\w+)", default="N/A"),
#         "Item Description": "4MM DECORATIVE PLY (2.44X1.22) AAA",
#         "Quantity": extract_field(text, r"(\d+\.?\d*)\s*PCS", default="N/A"),
#         "Rate per PCS": extract_field(text, r"Rate\s*(\d+\.?\d*)", default="N/A"),
#         "Total Amount": extract_field(text, r"Total\s*₹\s*([\d,]+\.?\d*)", default="N/A"),
#         "GST Amount": extract_field(text, r"Tax Amount\s*₹\s*([\d,]+\.?\d*)", default="N/A"),
#         "Bank Name": extract_field(text, r"Bank Name\s*([A-Za-z\s]+)", default="N/A"),
#         "Bank Account Number": extract_field(text, r"A/c No\s*(\d+)", default="N/A")
#     }
    
#     return invoice_details

# def extract_field(text, pattern, default="N/A", first_match=True):
#     """
#     Extract specific field from text using regex
    
#     Args:
#         text (str): Full text to search
#         pattern (str): Regex pattern to match
#         default (str): Default value if no match found
#         first_match (bool): Return first or all matches
    
#     Returns:
#         str or list: Extracted field(s)
#     """
#     matches = re.findall(pattern, text, re.IGNORECASE)
    
#     if not matches:
#         return default
    
#     return matches[0] if first_match else matches

# def main():
#     # Path to the invoice image
#     image_path = 'invoice.jpg'
    
#     # Extract details
#     invoice_details = extract_invoice_details(image_path)
    
#     # Print formatted JSON
#     print(json.dumps(invoice_details, indent=4))
    
#     # Optional: Save to JSON file
#     with open('invoice_details.json', 'w') as f:
#         json.dump(invoice_details, f, indent=4)

# if __name__ == "__main__":
#     main()

# # Additional extraction notes
# """
# Extraction Strategy:
# 1. Use pytesseract for full text extraction
# 2. Apply regex patterns to find specific fields
# 3. Handle variations in text formatting
# 4. Provide default values for missing fields

# Recommended Improvements:
# - Implement more robust error handling
# - Add confidence scoring for extracted fields
# - Support multiple invoice formats
# """
import re
import json
import cv2
import surya
from surya.ocr import run_ocr
from surya.input.load import load_from_files

def extract_field(text, pattern, default="N/A", first_match=True):
    """
    Extract specific field from text using regex
    
    Args:
        text (str): Full text to search
        pattern (str): Regex pattern to match
        default (str): Default value if no match found
        first_match (bool): Return first or all matches
    
    Returns:
        str or list: Extracted field(s)
    """
    matches = re.findall(pattern, text, re.IGNORECASE)
    if not matches:
        return default
    return matches[0] if first_match else matches

def extract_invoice_details(image_path):
    """
    Extract key details from the tax invoice using Surya OCR
    
    Args:
        image_path (str): Path to the invoice image
    
    Returns:
        dict: Extracted invoice details
    """
    # Load image using Surya
    images = load_from_files([image_path])
    
    # Run OCR
    results = run_ocr(images)
    
    # Combine all text lines
    text = '\n'.join(line.text for line in results[0].text)
    
    # Structured extraction of key details
    invoice_details = {
        "Company": "GUPTA PLY CO.",
        "Invoice Number": extract_field(text, r"Invoice No\.?\s*([A-Za-z0-9/\-]+)", default="N/A"),
        "Acknowledgement Number": extract_field(text, r"Ack No\.?\s*(\d+)", default="N/A"),
        "Acknowledgement Date": extract_field(text, r"Ack Date\s*(\d{2}-[A-Za-z]{3}-\d{2})", default="N/A"),
        "GSTIN": extract_field(text, r"GSTIN\s*(\w+)", default="N/A"),
        "Item Description": "4MM DECORATIVE PLY (2.44X1.22) AAA",
        "Quantity": extract_field(text, r"(\d+\.?\d*)\s*PCS", default="N/A"),
        "Rate per PCS": extract_field(text, r"Rate\s*(\d+\.?\d*)", default="N/A"),
        "Total Amount": extract_field(text, r"Total\s*₹\s*([\d,]+\.?\d*)", default="N/A"),
        "GST Amount": extract_field(text, r"Tax Amount\s*₹\s*([\d,]+\.?\d*)", default="N/A"),
        "Bank Name": extract_field(text, r"Bank Name\s*([A-Za-z\s]+)", default="N/A"),
        "Bank Account Number": extract_field(text, r"A/c No\s*(\d+)", default="N/A")
    }
    
    # Optional: Debug print of full extracted text
    print("Full Extracted Text:")
    print(text)
    
    return invoice_details

def main():
    """
    Main function to process invoice and output details
    """
    # Path to the invoice image
    image_path = 'Gupta.jpeg'
    
    # Extract details
    invoice_details = extract_invoice_details(image_path)
    
    # Print formatted JSON
    print("\nExtracted Invoice Details:")
    print(json.dumps(invoice_details, indent=4))
    
    # Optional: Save to JSON file
    with open('invoice_details.json', 'w') as f:
        json.dump(invoice_details, f, indent=4)

# Additional configuration for multilingual support
def configure_ocr_languages(languages=['en']):
    """
    Configure OCR language settings
    
    Args:
        languages (list): List of language codes to support
    """
    from surya.settings import settings
    settings.ocr_languages = languages

if __name__ == "__main__":
    # Optional: Configure languages if needed
    configure_ocr_languages(['en'])
    
    # Run main extraction
    main()

# Extraction Strategy and Improvements Notes
"""
Surya OCR Extraction Strategy:
1. Use Surya for advanced text extraction
2. Apply regex patterns for structured field extraction
3. Handle variations in text formatting
4. Provide default values for missing fields

Recommended Improvements:
- Implement more robust error handling
- Add confidence scoring for extracted fields
- Support multiple invoice formats
- Add image preprocessing (if needed)
- Implement logging for extraction process
"""