'''
    We have used LLaMA Vision 3.2 (11B) AI Model to create a simple web app
    that takes an image as input and generate a description of the image.
'''

# Start this app using: streamlit run web-app.py

import base64
import markdown2
import ollama
import streamlit as st

# Set page config
st.set_page_config(page_title="Image Description App", layout="centered")

# Add a title
st.title("Image Description Generator")

# Add file uploader
uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)

    # Add a button to generate description
    if st.button('Generate Description'):
        with st.spinner('Analyzing image...'):
            # Convert the Image into its Base64 Representation
            bytes_data = uploaded_file.getvalue()
            image_base64_str = base64.b64encode(bytes_data).decode("utf-8")

            # Invoke the Ollama API with the Base64 Image
            response = ollama.chat(
                model='llama3.2-vision:11b',
                messages=[{
                    'role': 'user',
                    'content': 'What is in this image?',
                    'images': [image_base64_str]
                }]
            )

            # Extract the description and display it
            description = markdown2.markdown(response.message.content)
            st.markdown(description, unsafe_allow_html=True)