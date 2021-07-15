###Create memes from text and images
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

####The application does the following tasks:
1) Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
2) Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
3) Load, manipulate, and save images.
4) Accept dynamic user input through a command-line tool, and a web service.


The sample quotes and images of Xander pup is located in 'src/_data/'.
A sample quote and author in "DogQuotesTXT.txt" would look like:

_"To bork or not to bork - Bork"_

_"He who smelt it... - Stinky"_

There is a simple Flask server which consumes all the modules and generates the meme over web.
The HTML templates are in /templates.

## Project Scaffolding
```
├── _data                       # Contains images and quotes.
├── MemeGenerator
│   ├── __init__.py   
│   ├── LilitaOne-Regular.ttf   # The font used 
│   ├── meme_engine.py          # Resizes the images and prints quotes on image
├── QuoteEngine
│    ├── __init__.py
│    ├── csvingestor.py         # Reads from csv
│    ├── docingestor.py         # Reads from docx
│    ├── engine.py              # Creates the QuoteModel object
│    ├── pdfingestor.py         # Reads from pdf
│    ├── textingestor.py        # Reads from text                 
├── static                      # folder to save the memes
├── templates                   # contains HTML templates                 
├── app.py                  
├── meme.py                    
├── Read.md                     # This file


```
Purpose of each of these files and folders:
_data - contains the quotes and images

meme_engine.py - Has make_meme() function which accepts the text , image path and author arguments.
The module crops the image to desired size and adds the text to image and saves the output image to folder.

csvingestor.py - This module reads the text and author from csv. The module make use of pandas library to read data from csv.

docingestor.py - this module reads the data from docx file. It makes use of docx libary.

engine.py - This module has the QuoteModel class which encapsulates body and author.
Also, the abstract class IngestorInterface.

pdfingestor.py - This module reads the data from pdf and converts it to text file, which is further used for processing.
This module make use of subprocess function with pdftotext package.

textingestor.py - This module reads data from .txt file.

static - This folder will have the output images.

app.py - The main module, which runs the meme generator over web.

meme.py - module which accepts command line arguments to create meme.

The various modules in detail:

#Quote Engine

The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:

"This is a quote body" - Author

###Ingestors
An abstract base class, IngestorInterface defines two methods with the following class method signatures:

def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]

Separate class would implement the parsing logic for each file type.
The responsibility of this module is to load and parse quotes from files.

#Meme Engine Module

The Meme Engine Module is responsible for manipulating and drawing text onto images.
The meme engine module does the following activities :

1)Loads image using Pillow package(PIL)
2)Resize the image as per the width which is 500 px and height is scaled proportionally.
3)Adds a quote body and author to image using ImageDraw.
4)Saves the output image to a folder.
5)These 4 steps are implemented inside the function,
make_meme(self, img_path, text, author, width=500) -> str #generated image path
The function returns the path to manipulated image.
6) The init method  take a required argument for where to save the generated images: 
   def __init__(self, output_dir)
   


Package the Application:
Use Python arg variables for CLI execution.The project contains a meme.py file that uses the MemeGenerator, TextIngestor, DocxIngestor, PDFIngestor, and CSVIngestor methods to generate a random captioned image.
The program is executable from the command line. The module takes three OPTIONAL arguments:

A string quote body
A string quote author
An image path

The program returns a path to a generated image. If any argument is not defined, a random selection is used.








