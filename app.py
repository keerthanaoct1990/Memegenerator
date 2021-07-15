"""Main app.py file.

The module which bind the text and author and image and display it in browser.
"""
import random
import os
import requests
from flask import Flask, render_template, request
from QuoteEngine import TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']


    quote = []
    ingestor_obj = Ingestor()
    for paths in quote_files:
        quote.extend(ingestor_obj.parse(paths))
    images_path = "./_data/photos/dog/"

    for root, dirs, files in os.walk(images_path):
        img = [os.path.join(root, name) for name in files]

    return quote, img


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    temp = requests.get(image_url, stream=True)
    temp_path = './temp_img.jpg'
    with open(temp_path, 'wb') as f:
        f.write(temp.content)
        path = meme.make_meme(temp_path, body, author)

    os.remove(temp_path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
