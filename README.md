# 🏦 Credit Card Statement Parser

A powerful web application that extracts and parses data from credit card PDF statements. Built with Flask and designed for maximum security with local processing.

## 🚀 Website Usage (Security-First Approach)

### Step-by-Step Usage Guide

1. **Visit the Website**
   ```
   https://parser-deepkothari.vercel.app/
   ```

2. **Clone the Repository Locally**
   ```bash
   git clone https://github.com/Deepkothari71/parser.git
   cd parser
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Local Server (For Security)**
   ```bash
   python app.py
   ```
   - This starts the Flask server on `http://localhost:5000`
   - **Important**: Keep this running while using the website

5. **Upload and Parse PDFs**
   - Go back to `https://parser-deepkothari.vercel.app/`
   - Click "Upload" or go to the upload page
   - Select your PDF statement
   - Click "Parse Statement"
   - The parsing happens on your local machine for maximum security

### 📋 Testing with Sample PDFs

For best results and testing, use the provided sample PDFs:

```bash
# Test with sample PDFs (recommended for first-time users)
python test_parser.py sample/hdfc.pdf
python test_parser.py sample/icici1.pdf
python test_parser.py sample/sbi1.pdf
python test_parser.py sample/icici2.pdf
python test_parser.py sample/sbi2.pdf
python test_parser.py sample/ae1.pdf
python test_parser.py sample/ae2.pdf
```

**Why use sample PDFs?**
- 🎯 **Guaranteed compatibility** - These PDFs are tested and work perfectly
- 📚 **Learning tool** - See exactly what data gets extracted
- 🔐 **No privacy concerns** - Sample data for testing purposes

### 🛡️ Security Benefits of This Approach

- **Local Processing**: All PDF parsing happens on your machine
- **No Cloud Storage**: Files never leave your computer
- **Privacy Protection**: Your financial data stays private
- **Full Control**: You control the entire parsing process

## 🎯 Features

### 🏛️ Multi-Bank Support

### 🔐 Security-First Design
- **Local Processing** - All PDF parsing happens on your local machine
- **No Cloud Storage** - Files are never stored on external servers
- **Temporary Processing** - Files are automatically deleted after parsing
- **Privacy Protection** - Your financial data never leaves your control

### ⚡ Key Capabilities
- **Lightning Fast** - Parse statements in under 5 seconds
- **Accurate Extraction** - Advanced text parsing algorithms
- **Multiple Format Output** - Export data as JSON or CSV
- **Modern UI** - Beautiful, responsive web interface
- **Drag & Drop** - Easy file upload with drag-and-drop support
- **Error Handling** - Comprehensive error messages and validation

### 📈 Extracted Data
- Cardholder Name
- Card Number (masked)
- Statement Period
- Total Amount Due
- Minimum Amount Due
- Due Date

### 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Deepkothari71/parser.git
   cd parser
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application locally**
   ```bash
   python app.py
   ```

4. **Open your browser**
   ```
   http://localhost:5000
   ```

## ⚙️ Development Setup

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask development server
python app.py

# The app will be available at http://localhost:5000
```


## 📂 Project Structure

```
parser/
├── app.py                 # Main Flask application
├── requirements.txt        # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── index.html            # Landing page
├── upload.html           # Upload interface
├── parsers/              # PDF parsing modules
│   ├── base_parser.py    # Base parser class
│   └── bank_parsers.py   # Bank-specific parsers
├── sample/               # Sample PDF files for testing
│   ├── hdfc.pdf
│   ├── icici1.pdf
│   ├── sbi1.pdf
│   └── ...
└── test_parser.py        # Testing script
```

## ⚙️ Configuration


## 🔌 API Endpoints

### POST `/api/parse`
Upload and parse a PDF statement
- **Input**: Multipart form with PDF file
- **Output**: JSON with extracted data
- **Example Response**:
  ```json
  {
    "Cardholder": "John Doe",
    "Card Number": "**** 1234",
    "Total Due": "₹15,230.45",
    "Due Date": "20 Oct 2025",
    "Bank": "HDFC"
  }
  ```

### POST `/api/download/<format>`
Download parsed data
- **Formats**: `json`, `csv`
- **Input**: JSON data
- **Output**: File download


## 🔧 Troubleshooting

### Common Issues

1. **"Connection error: Failed to fetch"**
   - Ensure Flask server is running locally
   - Check if port 5000 is available
   - Verify firewall settings

2. **"Could not parse the statement"**
   - PDF might be image-based (scanned)
   - Try with a text-based PDF
   - Check if the statement format is supported

3. **"File size exceeds limit"**
   - Reduce PDF file size
   - Maximum allowed: 5MB

### Debug Mode
```bash
# Run with debug information
python app.py
```


## 🗺️ Roadmap

- [ ] OCR support for scanned PDFs
- [ ] Additional bank support
- [ ] Batch processing



---

**⚠️ Important**: This tool processes sensitive financial documents. Always ensure you're running the latest version and review the code before use. For maximum security, run the backend locally and never store parsed data on external servers.
