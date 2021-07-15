from QuoteEngine import IngestorInterface
from QuoteEngine import DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor
from abc import abstractmethod


class Ingestor(IngestorInterface):
    """Ingestor class realize the IngestorInterface abstract base class."""


    def parse(self, path: str):
        """Select the appropriate helper for a given file based on filetype."""
        if path.endswith('.txt'):
            if TextIngestor.can_ingest(path):
                txt_ingestor = TextIngestor()
                return txt_ingestor.parse(path)
        elif path.endswith('.docx'):
            if DocxIngestor.can_ingest(path):
                doc_ingestor = DocxIngestor()
                return doc_ingestor.parse(path)
        elif path.endswith('.pdf'):
            if PDFIngestor.can_ingest(path):
                pdf_ingestor = PDFIngestor()
                return pdf_ingestor.parse(path)
        elif path.endswith('.csv'):
            if CSVIngestor.can_ingest(path):
                csv_ingestor = CSVIngestor()
                return csv_ingestor.parse(path)

