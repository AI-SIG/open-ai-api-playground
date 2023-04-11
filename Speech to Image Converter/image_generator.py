import openai
import requests
import os
import constants

# set environment key before we begin
# you can also set an os environment key but meh
openai.api_key = constants.OPEN_AI_API_KEY

class ImageGenerator:
    
    @staticmethod
    def generate_image_from_prompt(prompt):
        """
        Takes a prompt as text and generates an image using Dall-E. The image is stored in a directory called images
        as generated_image.png. Might make it fancy later. Might not
        """
        print("[Now generating image...]  " + prompt)
        image_dir_name = "images"
        image_dir = os.path.join(os.curdir, image_dir_name)
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)
        
        # print(f"{image_dir=}")

        generation_response = openai.Image.create(
            prompt=prompt,
            n=5,
            size="1024x1024",
            response_format="url",
        )
        # print(generation_response)

        generated_image_name = "generated_image.png" # the filetype should be .png
        generated_image_filepath = os.path.join(image_dir, generated_image_name)
        generated_image_url = generation_response["data"][0]["url"]  # extract image URL from response
        generated_image = requests.get(generated_image_url).content

        with open(generated_image_filepath, "wb") as image_file:
            image_file.write(generated_image)  # write the image to the file

# ImageGenerator.generate_image_from_prompt("The Golden Girls on crack")

