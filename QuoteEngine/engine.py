"""Meme engine module.

has the QuoteModel class which encapsulates body and author.
Also the abstract class IngestorInterface
"""
from abc import ABC, abstractmethod


class QuoteModel:
    """QuoteModel class contains text fields for body and author."""

    def __init__(self, body, author):
        """Initialize body and author.

        :param body: the text field
        :param author: the author
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Human readable string."""
        return f'{self.body} - {self.author}'


class IngestorInterface(ABC):
    """abstract base class, IngestorInterface."""

    @classmethod
    def can_ingest(cls, path):
        """Complete classmethod method to verify if the file type is compatible with the ingestor class.

        @:param path: path to the input document
        """
        return path.split('.')[-1] in ['txt', 'csv', 'pdf', 'docx']


    @abstractmethod
    def parse(self, path: str):
        """Abstract method for parsing the file content (i.e., splitting each row) and outputting it to a Quote object.

        @:param path : path of file to be parsed.
        """
        
        pass
