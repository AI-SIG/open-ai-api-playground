import speech_converter as sc
import image_generator as ig

def main():
    prompt = sc.SpeechConverter.get_prompt_from_speech()
    ig.ImageGenerator.generate_image_from_prompt(prompt)

if __name__ == "__main__":
    main()    