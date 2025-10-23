import re
from pdfminer.high_level import extract_text

# Try optional import of PyMuPDF. Many serverless platforms (like Vercel)
# don't provide the native dependencies required by PyMuPDF. We keep this
# import optional so the module can still load and fall back to pdfminer.
try:  # type: ignore
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except Exception:
    fitz = None  # type: ignore
    PYMUPDF_AVAILABLE = False

class BaseParser:
    """Base class for all bank-specific parsers"""
    
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self.extract_text()
    
    def extract_text(self):
        """Extract text from PDF. Prefer PyMuPDF if available; fall back to pdfminer."""
        # Use PyMuPDF only if it imported successfully
        if PYMUPDF_AVAILABLE:
            try:
                doc = fitz.open(self.pdf_path)  # type: ignore
                text = ""
                for page in doc:
                    text += page.get_text()
                doc.close()
                return text
            except Exception as e:
                print(f"PyMuPDF failed, trying pdfminer: {e}")

        # Fallback to pdfminer (pure-Python, serverless-friendly)
        try:
            return extract_text(self.pdf_path)
        except Exception as e2:
            print(f"pdfminer failed: {e2}")
            return ""
    
    def extract_with_regex(self, pattern, default="Not Found"):
        """Extract data using regex pattern"""
        match = re.search(pattern, self.text, re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()
        return default
    
    def extract_amount(self, pattern, default="₹0.00"):
        """Extract amount and format it"""
        match = re.search(pattern, self.text, re.IGNORECASE | re.MULTILINE)
        if match:
            amount = match.group(1).strip()
            # Clean up amount (remove extra spaces, commas)
            amount = re.sub(r'\s+', '', amount)
            # Ensure it has rupee symbol
            if not amount.startswith('₹'):
                amount = '₹' + amount
            return amount
        return default
    
    def extract_date(self, pattern, default="Not Found"):
        """Extract date from text"""
        match = re.search(pattern, self.text, re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()
        return default
    
    def parse(self):
        """Override this method in child classes"""
        raise NotImplementedError("Each parser must implement parse()")
