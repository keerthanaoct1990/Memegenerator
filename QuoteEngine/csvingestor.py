"""Module which parses the content from csv file."""
from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):
    """Class inherits the IngestorInterface."""


    def parse(self, path: str):
        """Parse the csv file.

        @:param path: path to csv file
        The parse method returns a valid QuoteModel.
        """
        if self.can_ingest(path):
            list_obj = []
            df = pd.read_csv(path)
            body = df['body']
            author = df['author']
            list_obj.append(QuoteModel(body[0].strip(), author[0].strip()))
            list_obj.append(QuoteModel(body[1].strip(), author[1].strip()))
            return list_obj
