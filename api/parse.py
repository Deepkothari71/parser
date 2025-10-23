import json
import os
import sys
import tempfile
from http.server import BaseHTTPRequestHandler
import urllib.parse

# Add the parent directory to the path so we can import parsers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parsers.bank_parsers import detect_bank_and_parse

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Get content length
            content_length = int(self.headers.get('Content-Length', 0))
            
            # Read the request body
            post_data = self.rfile.read(content_length)
            
            # Parse multipart form data
            boundary = None
            for header, value in self.headers.items():
                if header.lower() == 'content-type':
                    if 'boundary=' in value:
                        boundary = value.split('boundary=')[1]
                        break
            
            if not boundary:
                self.send_error_response(400, 'No boundary found in Content-Type')
                return
            
            # Parse the multipart data
            file_data = self.parse_multipart(post_data, boundary)
            
            if not file_data:
                self.send_error_response(400, 'No file provided')
                return
            
            # Save file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(file_data)
                filepath = tmp_file.name
            
            try:
                # Parse the PDF
                result = detect_bank_and_parse(filepath)
                
                if result is None:
                    self.send_error_response(400, 'Could not parse the statement. The PDF may be scanned/image-based or format is not recognized.')
                    return
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode())
                
            except Exception as e:
                self.send_error_response(500, f'Error parsing PDF: {str(e)}')
            
            finally:
                # Clean up
                if os.path.exists(filepath):
                    os.remove(filepath)
                    
        except Exception as e:
            self.send_error_response(500, f'Server error: {str(e)}')
    
    def do_OPTIONS(self):
        # Handle CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def parse_multipart(self, data, boundary):
        """Simple multipart parser to extract file data"""
        boundary_bytes = f'--{boundary}'.encode()
        parts = data.split(boundary_bytes)
        
        for part in parts:
            if b'Content-Disposition: form-data' in part and b'filename=' in part:
                # Find the file data (after the headers)
                header_end = part.find(b'\r\n\r\n')
                if header_end != -1:
                    file_data = part[header_end + 4:]
                    # Remove trailing boundary markers
                    if file_data.endswith(b'\r\n'):
                        file_data = file_data[:-2]
                    return file_data
        return None
    
    def send_error_response(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        error_response = json.dumps({'error': message})
        self.wfile.write(error_response.encode())