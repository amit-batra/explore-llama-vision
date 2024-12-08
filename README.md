# Explore LLaMA Vision
We have created a Flask-based simple Python web-app that lets the user upload an image, and then use the Ollama client API to generate a description for the image using LLaMA 3.2 Vision (11B parameters) AI model.

# Running Locally
You need the following on your machine to run this app locally:
1. Clone this repository: `git clone git@github.com:amit-batra/explore-llama-vision.git`.
2. Install Ollama utility from https://ollama.com/.
3. Ensure that you have a functional Python 3 installation (we tested this app with Python 3.12). On macOS, you can use Homebrew to install Python 3.12 like so: `brew install python@3.12`.
4. Create a Python virtual environment and activate it with these commands:
   1. `cd explore-llama-vision`
   2. `python3 -m venv .venv`
   3. `source .venv/bin/activate`
5. Now install the required Python libraries inside your virtual environment with these commands:
   1. `pip install --upgrade pip`
   2. `pip install ollama flask pillow`
6. At this point, you should see the name of the virtual environment printed in brackets `(.venv)` before your actual command prompt.
7. Launch the web-app using this command: `python3 with-flask-web-app.py` and navigate to https://localhost:5000/ to try it out.
8. We also have a command-line app that can be run using: `python3 with-single-image.py`.
9. Deactivate your Python virtual environment using the command `deactivate`.
