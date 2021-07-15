"""Module which parses the content from docx file."""
from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel
import subprocess
import random


class PDFIngestor(IngestorInterface):
    """Class inherits the IngestorInterface."""


    def parse(self, path: str):
        """Parse the pdf file.

        @:param path: path to pdf file
        The parse method returns a valid QuoteModel.
        """
        if self.can_ingest(path):
            tmp = f'./_data/DogQuotes/pdftext{random.randint(0, 1000000)}.txt'
            call = subprocess.call(['./_data/DogQuotes/pdftotext', '-layout', path, tmp])
            try:
                file_ref = open(tmp, "r")
            except IOError:
                print("Error: File does not appear to exist.")
            list_obj = []
            for line in file_ref:
                if len(line) > 2:
                    content = line.split('-')
                    list_obj.append(QuoteModel(content[0].strip(), content[1].strip()))
            return list_obj

