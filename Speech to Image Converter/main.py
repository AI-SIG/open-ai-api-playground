import speech_converter as sc
import image_generator as ig

# Install python-pip if it isn't installed
# Use pip install -r requirements.txt to install all dependencies.
# NB this has not been tested so cthulhuspeed

def main():
    prompt = sc.SpeechConverter.get_prompt_from_speech()
    ig.ImageGenerator.generate_image_from_prompt(prompt)
    
if __name__ == "__main__":
    main()