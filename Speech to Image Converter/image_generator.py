import openai
import requests
import os
import constants
# from PIL import Image

# set environment key
openai.api_key = constants.OPEN_AI_API_KEY

class ImageGenerator:
    @staticmethod
    def generate_image_from_prompt(prompt):
        image_dir_name = "images"
        image_dir = os.path.join(os.curdir, image_dir_name)
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)
        
        print(f"{image_dir=}")

        generation_response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url",
        )
        print(generation_response)

ImageGenerator.generate_image_from_prompt("The Golden Girls on crack")

