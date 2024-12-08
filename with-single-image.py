'''
    We have used LLaMA Vision 3.2 (11B) AI Model to create a simple app
    that takes an image as input and generate a description of the image.
'''

# Start this app using: python3 with-single-image.py

import base64
import ollama
import requests
from io import BytesIO
from PIL import Image

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

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg"
image, image_base64 = image_url_to_base64(url)

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