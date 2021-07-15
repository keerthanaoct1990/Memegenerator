"""Module which parses the content from docx file."""
from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel


class TextIngestor(IngestorInterface):
    """Class inherits the IngestorInterface."""


    def parse(self, path: str):
        """Parse the text file.

        @:param path: path to text file
        The parse method returns a valid QuoteModel.
        """
        if self.can_ingest(path):
            list_obj = []
            try:
                f_text = open(path, encoding="charmap")
            except IOError:
                print("Error: File does not appear to exist.")

            for line in f_text:
                encoded_string = line.encode("ascii", "ignore")
                line = encoded_string.decode()
                content = line.split('-')
                list_obj.append(QuoteModel(content[0].strip(), content[1].strip()))
            return list_obj

