"""Module which parses the content from docx file."""
from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """Class inherits the IngestorInterface."""


    def parse(self, path: str):
        """Parse the docx file.

        @:param path: path to docx file
        The parse method returns a valid QuoteModel.
        """
        if self.can_ingest(path):
            list_obj = []
            doc = docx.Document(path)
            all_paras = doc.paragraphs
            for line in all_paras:
                if line.text:
                    content = line.text.split('-')
                    list_obj.append(QuoteModel(content[0].strip(), content[1].strip()))
            return list_obj
