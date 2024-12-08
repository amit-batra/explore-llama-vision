'''
    We have used LLaMA Vision 3.2 (11B) AI Model to create a simple web app
    that takes an image as input and generate a description of the image.
'''

# Start this app using: python3 with-flask-web-app.py

import base64
import ollama
from flask import Flask, request, render_template
    
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        # Convert the Image into its Base64 Representation
        image_base64_str = base64.b64encode(file.read()).decode("utf-8")

        # Invoke the Ollama API with the Base64 Image
        response = ollama.chat(
            model='llama3.2-vision:11b',
            messages=[{
                'role': 'user',
                'content': 'What is in this image?',
                'images': [image_base64_str]
            }]
        )

        # Extract the description from the Ollama response
        description = response.message.content

        # Render HTML with the image description
        return render_template('index.html', description=description) # f"<h1>Description:</h1><p>{description}</p>"

if __name__ == "__main__":
    app.run(debug=True)
