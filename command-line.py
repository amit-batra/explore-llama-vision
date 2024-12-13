'''
    We have used LLaMA Vision 3.2 (11B) AI Model to create a simple app
    that takes an image as input and generate a description of the image.
'''

# Start this app using: python3 command-line.py <image_path_or_url>

import base64
import ollama
import requests
import sys
from io import BytesIO
from PIL import Image
from urllib.parse import urlparse

def is_url(string):
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except:
        return False

def image_url_to_base64(url):
    try:
        # Step 1: Fetch the image from the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error if the request fails

        # Step 2: Open the image using PIL
        image = Image.open(BytesIO(response.content))

        # Step 3: Encode the byte stream into a base64 string
        img_base64 = base64.b64encode(response.content).decode("utf-8")

        # Step 4: Return both the Image and its Base64 representation
        return image, img_base64

    except Exception as e:
        print("Error occurred:", e)
        return None, None

def image_file_to_base64(file_path):
    try:
        # Step 1: Open and read the image file
        image_file = open(file_path, 'rb')

        # Step 2: Read the image using PIL
        image = Image.open(image_file)

        # Step 3: Go back to start of file after file read
        image_file.seek(0)

        # Step 4: Get base64 encoding
        img_base64 = base64.b64encode(image_file.read()).decode('utf-8')

        # Step 5: Return both the Image and its Base64 representation
        return image, img_base64

    except Exception as e:
        print("Error occurred:", e)
        return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 command-line.py <image_path_or_url>")
        sys.exit(1)

    input_path = sys.argv[1]

    if is_url(input_path):
        image, image_base64 = image_url_to_base64(input_path)
    else:
        image, image_base64 = image_file_to_base64(input_path)

    if image is None or image_base64 is None:
        print("Failed to process the image. Please check if the path/URL is correct.")
        sys.exit(1)

    response = ollama.chat(
        model='llama3.2-vision:11b',
        messages=[{
            'role': 'user',
            'content': 'What is in this image?',
            'images': [image_base64]
        }]
    )
    image.show()
    print(response.message.content)

if __name__ == "__main__":
    main()