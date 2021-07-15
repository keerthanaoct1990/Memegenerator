"""The module crops the image and add quotes to image."""
from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine:
    """Class creates the meme."""

    def __init__(self, output_dir):
        """Initialize the output path."""
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)


    def make_meme(self, img_path, text, author, width=500):
        """Create the meme.

        @:param img_path : path of input image
        @:param text : the text that has to be added to image
        @:param author : the author of text
        @:param width : width of output image

        Return the output image path.
        """

        img = Image.open(img_path)


        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        new_img = img.resize((width, height))

        if text is not None:
            draw = ImageDraw.Draw(new_img)
            try:
                font = ImageFont.truetype('./MemeGenerator/LilitaOne-Regular.ttf', size=20)
            except OSError:
                print("The font doesn't exist")
            text = f'{text} - {author}'
            draw.text((10, 30), text, font=font, fill='white')
        out_path = f'{self.output_dir}/{str(random.randint(10000, 99999))}.jpg'
        new_img.save(out_path)
        return out_path


