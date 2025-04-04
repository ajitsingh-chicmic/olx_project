# from PIL import Image
# import pytesseract
# print(pytesseract.image_to_string(Image.open('image.png')))
# from paddleocr import PaddleOCR

# ocr = PaddleOCR(use_angle_cls=True, lang='en')
# result = ocr.ocr('chicmic.jpg', cls=True)

# for line in result[0]:
#     print(f"Detected text: {line[1]}")
# Install required packages first:
# pip install paddlepaddle
# pip install paddleocr

# from paddleocr import PaddleOCR, draw_ocr
# import cv2
# import os
# import matplotlib.pyplot as plt

# def perform_ocr(image_path, output_folder=None, use_gpu=False, lang='en'):
#     """
#     Perform OCR on an image using PaddleOCR.
    
#     Args:
#         image_path (str): Path to the image file
#         output_folder (str, optional): Folder to save visualization results
#         use_gpu (bool): Whether to use GPU acceleration
#         lang (str): Language code ('en', 'ch', etc.)
        
#     Returns:
#         list: List of OCR results
#     """
#     # Create OCR instance
#     ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=use_gpu)
    
#     # Read the image
#     img = cv2.imread(image_path)
    
#     # Detect and recognize text
#     result = ocr.ocr(image_path, cls=True)
    
#     # Print OCR results
#     print("Text Recognition Results:")
#     for idx, line in enumerate(result):
#         print(f"Line {idx+1}: {line[1][0]} (Confidence: {line[1][1]:.4f})")
    
#     # Visualize results if output folder is provided
#     if output_folder:
#         os.makedirs(output_folder, exist_ok=True)
#         output_path = os.path.join(output_folder, os.path.basename(image_path))
        
#         # Draw OCR results on image
#         boxes = [line[0] for line in result]
#         txts = [line[1][0] for line in result]
#         scores = [line[1][1] for line in result]
        
#         # Visualize with font
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         font_path = './fonts/simfang.ttf'  # Provide a default font or download one
#         im_show = draw_ocr(img, boxes, txts, scores, font_path=font_path)
        
#         plt.figure(figsize=(10, 10))
#         plt.imshow(im_show)
#         plt.axis('off')
#         plt.savefig(output_path)
#         plt.close()
        
#         print(f"Visualization saved to {output_path}")
    
#     return result

# # Example usage
# if __name__ == "__main__":
#     # Path to your image
#     image_path = "image.png"
    
#     # Perform OCR
#     result = perform_ocr(
#         image_path=image_path,
#         output_folder="./ocr_results",
#         use_gpu=False,  # Set to True if GPU is available
#         lang='en'       # Language code ('en', 'ch', etc.)
#     )
    
#     # Extract text only
#     all_text = []
#     for line in result:
#         all_text.append(line[1][0])
    
#     full_text = '\n'.join(all_text)
#     print("\nExtracted Text:")
#     print(full_text)
# Install required packages first:
# pip install paddlepaddle
# pip install paddleocr

# from paddleocr import PaddleOCR, draw_ocr
# import cv2
# import os
# import matplotlib.pyplot as plt

# def perform_ocr(image_path, output_folder=None, use_gpu=False, lang='en'):
#     """
#     Perform OCR on an image using PaddleOCR.
    
#     Args:
#         image_path (str): Path to the image file
#         output_folder (str, optional): Folder to save visualization results
#         use_gpu (bool): Whether to use GPU acceleration
#         lang (str): Language code ('en', 'ch', etc.)
        
#     Returns:
#         list: List of OCR results
#     """
#     # Create OCR instance
#     ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=use_gpu)
    
#     # Read the image
#     img = cv2.imread(image_path)
    
#     # Detect and recognize text
#     result = ocr.ocr(image_path, cls=True)
    
#     # Print OCR results
#     print("Text Recognition Results:")
#     for idx, line in enumerate(result):
#         print(f"Line {idx+1}: {line[1][0]} (Confidence: {line[1][1]:.4f})")
    
#     # Visualize results if output folder is provided
#     if output_folder:
#         os.makedirs(output_folder, exist_ok=True)
#         output_path = os.path.join(output_folder, os.path.basename(image_path))
        
#         # Draw OCR results on image
#         boxes = [line[0] for line in result]
#         txts = [line[1][0] for line in result]
#         scores = [line[1][1] for line in result]
        
#         # Visualize with font
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         font_path = './fonts/simfang.ttf'  # Provide a default font or download one
#         im_show = draw_ocr(img, boxes, txts, scores, font_path=font_path)
        
#         plt.figure(figsize=(10, 10))
#         plt.imshow(im_show)
#         plt.axis('off')
#         plt.savefig(output_path)
#         plt.close()
        
#         print(f"Visualization saved to {output_path}")
    
#     return result

# # Example usage
# if __name__ == "__main__":
#     # Path to your image
#     image_path = "chicmic.jpg"
    
#     # Perform OCR
#     result = perform_ocr(
#         image_path=image_path,
#         output_folder="./ocr_results",
#         use_gpu=False,  # Set to True if GPU is available
#         lang='en'       # Language code ('en', 'ch', etc.)
#     )
    
#     # Extract text only
#     all_text = []
#     for line in result:
#         all_text.append(line[1][0])
    
#     full_text = '\n'.join(all_text)
#     print("\nExtracted Text:")
#     print(full_text)
# from paddleocr import PaddleOCR, draw_ocr
# import cv2
# import os
# import matplotlib.pyplot as plt
# import numpy as np

# def perform_ocr(image_path, output_folder=None, use_gpu=False, lang='en'):
#     """
#     Perform OCR on an image using PaddleOCR.
    
#     Args:
#         image_path (str): Path to the image file
#         output_folder (str, optional): Folder to save visualization results
#         use_gpu (bool): Whether to use GPU acceleration
#         lang (str): Language code ('en', 'ch', etc.)
        
#     Returns:
#         list: List of OCR results
#     """
#     # Create OCR instance
#     ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=use_gpu)
    
#     # Read the image
#     img = cv2.imread(image_path)
#     if img is None:
#         print(f"Error: Could not read image at {image_path}")
#         return []
    
#     # Detect and recognize text
#     result = ocr.ocr(image_path, cls=True)
    
#     # Print OCR results - with proper error handling for different result formats
#     print("Text Recognition Results:")
#     if result is None or len(result) == 0:
#         print("No text detected in the image.")
#         return []
    
#     # Handle different PaddleOCR versions which might return different structured results
#     # For PaddleOCR >= 2.6.0, results are wrapped in an additional list
#     if isinstance(result, list) and len(result) > 0 and isinstance(result[0], list):
#         result = result[0]
    
#     for idx, line in enumerate(result):
#         # Safely print the results by checking the structure
#         try:
#             if isinstance(line, tuple) and len(line) >= 2:
#                 # Handle case where line is a tuple of (box_coordinates, (text, confidence))
#                 if isinstance(line[1], tuple) and len(line[1]) >= 2:
#                     text, confidence = line[1]
#                     print(f"Line {idx+1}: {text} (Confidence: {confidence:.4f})")
#                 # Handle case where line[1] is just the text
#                 else:
#                     print(f"Line {idx+1}: {line[1]}")
#             else:
#                 print(f"Line {idx+1}: {line}")
#         except Exception as e:
#             print(f"Error processing line {idx+1}: {e}")
#             print(f"Line content: {line}")
    
#     # Visualize results if output folder is provided
#     if output_folder and result:
#         os.makedirs(output_folder, exist_ok=True)
#         output_path = os.path.join(output_folder, os.path.basename(image_path))
        
#         try:
#             # Extract boxes, texts, and scores with error handling
#             boxes = []
#             txts = []
#             scores = []
            
#             for line in result:
#                 try:
#                     if isinstance(line, tuple) and len(line) >= 2:
#                         # Get box coordinates
#                         if isinstance(line[0], np.ndarray):
#                             boxes.append(line[0])
#                         elif isinstance(line[0], list):
#                             boxes.append(np.array(line[0]))
#                         else:
#                             continue
                        
#                         # Get text and confidence
#                         if isinstance(line[1], tuple) and len(line[1]) >= 2:
#                             txts.append(line[1][0])
#                             scores.append(line[1][1])
#                         elif isinstance(line[1], str):
#                             txts.append(line[1])
#                             scores.append(0.5)  # Default confidence if not provided
#                 except Exception as e:
#                     print(f"Error processing visualization line: {e}")
#                     continue
            
#             if boxes and txts:
#                 # Convert image to RGB for display
#                 img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
#                 # Try to use font if available, otherwise use default
#                 try:
#                     font_path = './fonts/simfang.ttf'
#                     if not os.path.exists(font_path):
#                         # Try to find a system font
#                         system_fonts = [
#                             '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
#                             '/usr/share/fonts/TTF/DejaVuSans.ttf',
#                             '/System/Library/Fonts/Supplemental/Arial.ttf',
#                             'C:/Windows/Fonts/arial.ttf'
#                         ]
#                         for f in system_fonts:
#                             if os.path.exists(f):
#                                 font_path = f
#                                 break
                    
#                     # Draw OCR results on image
#                     im_show = draw_ocr(img, boxes, txts, scores, font_path=font_path)
                    
#                     plt.figure(figsize=(10, 10))
#                     plt.imshow(im_show)
#                     plt.axis('off')
#                     plt.savefig(output_path)
#                     plt.close()
                    
#                     print(f"Visualization saved to {output_path}")
#                 except Exception as e:
#                     print(f"Error during visualization: {e}")
#         except Exception as e:
#             print(f"Error during visualization process: {e}")
    
#     return result

# # Example usage
# if __name__ == "__main__":
#     # Path to your image
#     image_path = "chicmic.jpg"
    
#     # Perform OCR
#     result = perform_ocr(
#         image_path=image_path,
#         output_folder="./ocr_results",
#         use_gpu=False,  # Set to True if GPU is available
#         lang='en'       # Language code ('en', 'ch', etc.)
#     )
    
#     # Extract text only
#     all_text = []
    
#     # Handle different PaddleOCR versions
#     if isinstance(result, list) and len(result) > 0:
#         for line in result:
#             try:
#                 if isinstance(line, tuple) and len(line) >= 2:
#                     if isinstance(line[1], tuple) and len(line[1]) >= 1:
#                         all_text.append(line[1][0])
#                     elif isinstance(line[1], str):
#                         all_text.append(line[1])
#                 else:
#                     # Try to extract text based on the actual structure
#                     text = str(line)
#                     all_text.append(text)
#             except Exception as e:
#                 print(f"Error extracting text: {e}")
    
#     if all_text:
#         full_text = '\n'.join(all_text)
#         print("\nExtracted Text:")
#         print(full_text)
#     else:
#         print("\nNo text could be extracted")
# from paddleocr import PaddleOCR

# # Initialize PaddleOCR
# ocr = PaddleOCR(use_angle_cls=True, lang='en')

# # Perform OCR on the image
# result = ocr.ocr('weight.jpg', cls=True)

# # Initialize a list to hold the filtered results
# filtered_results = []

# # Loop through the detected lines
# for line in result[0]:
#     text, score = line[1]
#     # Filter based on confidence score (e.g., only keep scores above 0.95)
#     if score > 0.95:
#         filtered_results.append({
#             "text": text,
#             "confidence": score
#         })

# # Print or save the filtered results (e.g., save to a JSON file)
# import json
# with open('filtered_results.json', 'w') as f:
#     json.dump(filtered_results, f, indent=4)

# print("Filtered Results:", filtered_results)
# from PIL import Image
# from surya_functions import get_image_tex
# image = Image.open(uploaded_file)
# import json
# import re

# # Load the OCR data (assuming the JSON is stored in 'ocr_data')
# with open("results.json", "r") as f:
#     data = json.load(f)

# # Function to extract key-value pairs
# def extract_key_values(data):
#     key_value_pairs = {}
#     text_lines = data["chicmic"][0]["text_lines"]

#     # Iterate through each detected text line
#     for i, line in enumerate(text_lines):
#         text = line["text"].strip()

#         # Check for "key: value" format
#         if ":" in text:
#             key, value = map(str.strip, text.split(":", 1))
#             key_value_pairs[key] = value

#         # Handle multi-line key-value (key in one line, value in next)
#         elif i < len(text_lines) - 1:
#             next_text = text_lines[i + 1]["text"].strip()
#             if re.search(r"(invoice|gst|total|date|amount|account|number)", text, re.IGNORECASE):
#                 key_value_pairs[text] = next_text

#     return key_value_pairs

# # Extract key-value pairs
# key_values = extract_key_values(data)

# # Display results
# for key, value in key_values.items():
#     print(f"{key}: {value}")


# import json
# from transformers import LayoutLMv3Processor, LayoutLMv3ForTokenClassification
# from PIL import Image
# import torch

# # Load the pre-trained model and processor
# processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
# model = LayoutLMv3ForTokenClassification.from_pretrained("microsoft/layoutlmv3-base")

# # Load OCR output (results.json) and the original image
# with open("results.json", "r") as f:
#     ocr_data = json.load(f)

# image = Image.open("Gupta.jpeg")

# # Extract text and bounding boxes from OCR output
# text_lines = ocr_data["Gupta"][0]["text_lines"]
# texts = [line["text"] for line in text_lines]
# bboxes = [line["bbox"] for line in text_lines]

# # Normalize bounding boxes (for LayoutLM input)
# width, height = image.size
# normalized_bboxes = [[
#     int(1000 * (x / width)),
#     int(1000 * (y / height)),
#     int(1000 * (x2 / width)),
#     int(1000 * (y2 / height))
# ] for (x, y, x2, y2) in bboxes]
# # for bb in normalized_bboxes:
# #     print(bb) 
# # Prepare the input for the model
# inputs = processor(image, texts, boxes=normalized_bboxes, return_tensors="pt")

# # Perform inference
# outputs = model(**inputs)

# # Map predictions to labels
# predicted_labels = outputs.logits.argmax(-1).squeeze().tolist()

# # Extract key-value pairs
# key_value_pairs = {}
# for i, (text, label) in enumerate(zip(texts, predicted_labels)):
#     if label == 1:  # 1 usually indicates a key
#         next_value = texts[i + 1] if i + 1 < len(texts) else None
#         key_value_pairs[text] = next_value

# # Print key-value pairs
# print(json.dumps(key_value_pairs, indent=2))

# import torch
# from transformers import LayoutLMv3Processor, LayoutLMv3ForTokenClassification
# from PIL import Image

# # Load the processor and model
# processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base")
# model = LayoutLMv3ForTokenClassification.from_pretrained("microsoft/layoutlmv3-base")

# # Ensure we use GPU if available
# device = "cuda" if torch.cuda.is_available() else "cpu"
# model.to(device)

# # Load the invoice image
# image_path = "Gupta.jpeg"
# image = Image.open(image_path)

# # Apply OCR to extract text and bounding boxes
# ocr_result = processor(images=image, return_tensors="pt", apply_ocr=True)

# for text, box in zip(ocr_result['text'], ocr_result['bbox']):
#     print(f"Text: {text}, Bounding Box: {box}")
# def extract_key_value_pairs(ocr_result, keywords, direction="right"):
#     key_value_pairs = {}

#     for keyword in keywords:
#         for i, text in enumerate(ocr_result['text']):
#             if keyword.lower() in text.lower():
#                 print(f"Found Keyword: {keyword} at {ocr_result['bbox'][i]}")

#                 # Find the closest value based on the direction
#                 if direction == "right":
#                     value = find_closest_right(ocr_result, i)
#                 elif direction == "down":
#                     value = find_closest_down(ocr_result, i)

#                 key_value_pairs[keyword] = value

#     return key_value_pairs


# def find_closest_right(ocr_result, index):
#     current_box = ocr_result['bbox'][index]
#     candidates = [
#         (ocr_result['text'][i], ocr_result['bbox'][i])
#         for i in range(len(ocr_result['text']))
#         if ocr_result['bbox'][i][1] == current_box[1] and ocr_result['bbox'][i][0] > current_box[2]
#     ]
#     candidates.sort(key=lambda x: x[1][0])  # Sort by x-axis (left-right)
#     return candidates[0][0] if candidates else None


# def find_closest_down(ocr_result, index):
#     current_box = ocr_result['bbox'][index]
#     candidates = [
#         (ocr_result['text'][i], ocr_result['bbox'][i])
#         for i in range(len(ocr_result['text']))
#         if ocr_result['bbox'][i][0] == current_box[0] and ocr_result['bbox'][i][1] > current_box[3]
#     ]
#     candidates.sort(key=lambda x: x[1][1])  # Sort by y-axis (top-down)
#     return candidates[0][0] if candidates else None
# # Define the keywords you want to extract
# keywords = ["Invoice Number", "Date", "Amount", "Bill to", "Due"]

# # Get key-value pairs
# key_value_data = extract_key_value_pairs(ocr_result, keywords)

# # Output extracted data in JSON format
# import json
# print(json.dumps(key_value_data, indent=4))
# import json

# # Load OCR output
# with open('results.json', 'r') as f:
#     ocr_data = json.load(f)

# # Extract text lines
# text_lines = ocr_data["Gupta"][0]["text_lines"]

# # Function to find the value near the keyword (Right if colon, otherwise Below)
# def find_value_nearby(keyword):
#     for i, line in enumerate(text_lines):
#         if keyword.lower() in line["text"].lower():
#             print(f"Found '{keyword}' at: {line['bbox']}")

#             # Check if keyword has a colon, implying value is on the right
#             if ":" in line["text"]:
#                 return find_value_to_right(line)
#             else:
#                 return find_value_below(line)

#     return "Value not found"


# # Find the nearest value to the right
# def find_value_to_right(keyword_line):
#     keyword_x = keyword_line["bbox"][2]  # Right edge of the keyword
#     keyword_y = keyword_line["bbox"][1]  # Y-axis position

#     candidates = [
#         (l["text"], l["bbox"]) for l in text_lines
#         if l["bbox"][0] > keyword_x and abs(l["bbox"][1] - keyword_y) < 20
#     ]

#     # Sort candidates by horizontal distance (left to right)
#     candidates.sort(key=lambda x: x[1][0])
#     return candidates[0][0] if candidates else "Value not found"


# # Find the nearest value below
# def find_value_below(keyword_line):
#     keyword_x = keyword_line["bbox"][0]
#     keyword_y = keyword_line["bbox"][3]  # Bottom of the keyword

#     candidates = [
#         (l["text"], l["bbox"]) for l in text_lines
#         if l["bbox"][1] > keyword_y and abs(l["bbox"][0] - keyword_x) < 50
#     ]

#     # Sort candidates by vertical distance (top to bottom)
#     candidates.sort(key=lambda x: x[1][1])
#     return candidates[0][0] if candidates else "Value not found"


# # Keywords to search for
# keywords_to_find = ["Invoice No.", "Ack Date", "GSTIN/UIN", "Amount"]

# # Extract key-value pairs
# extracted_data = {keyword: find_value_nearby(keyword) for keyword in keywords_to_find}

# # Display the extracted information
# print(json.dumps(extracted_data, indent=4))
import json
import difflib

class OCRKeyValueExtractor:
    def __init__(self, ocr_data):
        """
        Initialize the extractor with OCR data
        
        Args:
            ocr_data (dict): JSON-loaded OCR results
        """
        self.text_lines = ocr_data["Gupta"][0]["text_lines"]
    
    def find_value_nearby(self, keyword):
        """
        Find value near a keyword, considering context
        
        Args:
            keyword (str): Keyword to search for
        
        Returns:
            str: Extracted value or "Value not found"
        """
        # Find lines containing the keyword (fuzzy matching)
        matched_lines = [
            line for line in self.text_lines 
            if self._fuzzy_match(keyword.lower(), line["text"].lower())
        ]
        
        if not matched_lines:
            return "Value not found"
        
        # Take the first matched line
        keyword_line = matched_lines[0]
        
        # Check if keyword has a colon, implying value is on the right
        if ":" in keyword_line["text"]:
            return self._find_value_to_right(keyword_line)
        else:
            return self._find_value_below(keyword_line)
    
    def _find_value_to_right(self, keyword_line):
        """
        Find value to the right of a keyword
        
        Args:
            keyword_line (dict): Line containing the keyword
        
        Returns:
            str: Value found to the right
        """
        keyword_x = keyword_line["bbox"][2]  # Right edge of the keyword
        keyword_y = keyword_line["bbox"][1]  # Y-axis position
        
        # Find candidate values
        candidates = [
            (l["text"], l["bbox"]) for l in self.text_lines
            if (l["bbox"][0] > keyword_x and 
                abs(l["bbox"][1] - keyword_y) < 50)  # Adjust vertical tolerance
        ]
        
        # Sort candidates by horizontal distance
        candidates.sort(key=lambda x: x[1][0])
        
        return candidates[0][0] if candidates else "Value not found"
    
    def _find_value_below(self, keyword_line):
        """
        Find value below a keyword
        
        Args:
            keyword_line (dict): Line containing the keyword
        
        Returns:
            str: Value found below
        """
        keyword_x = keyword_line["bbox"][0]
        keyword_y = keyword_line["bbox"][3]  # Bottom of the keyword
        
        # Find candidate values
        candidates = [
            (l["text"], l["bbox"]) for l in self.text_lines
            if (l["bbox"][1] > keyword_y and 
                abs(l["bbox"][0] - keyword_x) < 50)  # Adjust horizontal tolerance
        ]
        
        # Sort candidates by vertical distance
        candidates.sort(key=lambda x: x[1][1])
        
        return candidates[0][0] if candidates else "Value not found"
    
    def _fuzzy_match(self, keyword, text, threshold=0.8):
        """
        Perform fuzzy matching for keywords
        
        Args:
            keyword (str): Keyword to match
            text (str): Text to match against
            threshold (float): Matching threshold
        
        Returns:
            bool: Whether the match is above the threshold
        """
        similarity = difflib.SequenceMatcher(None, keyword, text).ratio()
        return similarity >= threshold
    
    def extract_key_value_pairs(self, keywords):
        """
        Extract multiple key-value pairs
        
        Args:
            keywords (list): List of keywords to extract
        
        Returns:
            dict: Extracted key-value pairs
        """
        return {
            keyword: self.find_value_nearby(keyword) 
            for keyword in keywords
        }

def main():
    # Load OCR output
    with open('results.json', 'r') as f:
        ocr_data = json.load(f)
    
    # Keywords to search for
    keywords_to_find = [
        "Invoice No.", 
        "Ack Date", 
        "GSTIN/UIN", 
        "Amount"
    ]
    
    # Create extractor
    extractor = OCRKeyValueExtractor(ocr_data)
    
    # Extract key-value pairs
    extracted_data = extractor.extract_key_value_pairs(keywords_to_find)
    
    # Display the extracted information
    print(json.dumps(extracted_data, indent=4))

if __name__ == "__main__":
    main()