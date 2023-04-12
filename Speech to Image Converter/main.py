from speech_converter import SpeechConverter as sc
from image_generator import ImageGenerator as ig

# Install python-pip if it isn't installed
# Use pip install -r requirements.txt to install all dependencies.
# NB this has not been tested so cthulhuspeed

def main():
    prompt = sc.get_prompt_from_speech()
    ig.generate_image_from_prompt(prompt)
    
if __name__ == "__main__":
    main()