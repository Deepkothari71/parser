# 💳 Credit Card Statement Parser

A powerful web application that extracts and parses data from credit card PDF statements with support for major Indian banks. Built with Flask and designed for maximum security with local processing.

## ✨ Features

### 🏦 Multi-Bank Support
- **HDFC Bank** - Complete statement parsing
- **ICICI Bank** - Full data extraction
- **SBI (State Bank of India)** - Comprehensive parsing
- **Axis Bank** - Statement analysis
- **American Express** - Data extraction
- **PNB (Punjab National Bank)** - Statement parsing
- **Kotak Bank** - Full support
- **Yes Bank** - Complete parsing
- **IndusInd Bank** - Data extraction
- **Citibank** - Statement analysis
- **Standard Chartered** - Full support
- **HSBC** - Complete parsing
- **RBL Bank** - Statement analysis

### 🔒 Security-First Design
- **Local Processing** - All PDF parsing happens on your local machine
- **No Cloud Storage** - Files are never stored on external servers
- **Temporary Processing** - Files are automatically deleted after parsing
- **Privacy Protection** - Your financial data never leaves your control

### ⚡ Key Capabilities
- **Lightning Fast** - Parse statements in under 5 seconds
- **Accurate Extraction** - Advanced text parsing algorithms
- **Multiple Formats** - Export data as JSON or CSV
- **Modern UI** - Beautiful, responsive web interface
- **Drag & Drop** - Easy file upload with drag-and-drop support
- **Error Handling** - Comprehensive error messages and validation

### 📊 Extracted Data
- Cardholder Name
- Card Number (masked)
- Statement Period
- Total Amount Due
- Minimum Amount Due
- Due Date
- Credit Limit
- Available Credit
- Transaction Details
- Bank Information

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/parser.git
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

## 🔧 Development Setup

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask development server
python app.py

# The app will be available at http://localhost:5000
```

### Testing the Parser
```bash
# Test with a sample PDF
python test_parser.py sample/your_statement.pdf
```

## 🌐 Production Deployment

### Option 1: Local Server + Public Frontend (Recommended for Security)

For maximum security, run the backend locally and deploy only the frontend:

1. **Deploy Frontend to Vercel**
   - Push your code to GitHub
   - Connect to Vercel
   - Deploy the frontend files

2. **Run Backend Locally**
   ```bash
   python app.py
   ```

3. **Configure Frontend**
   - Update `upload.html` to point to your local server
   - Use your public IP or ngrok for external access

### Option 2: Full Cloud Deployment

For convenience (less secure):

1. **Deploy to Vercel**
   ```bash
   git add .
   git commit -m "Deploy to Vercel"
   git push
   ```

2. **Vercel will automatically deploy**
   - Visit your Vercel dashboard
   - Your app will be available at `https://your-app.vercel.app`

## 📁 Project Structure

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

## 🛠️ Configuration

### Environment Variables
Create a `.env` file for configuration:
```env
FLASK_ENV=development
MAX_FILE_SIZE=5242880  # 5MB in bytes
UPLOAD_FOLDER=uploads
```

### Security Settings
- Maximum file size: 5MB
- Allowed file types: PDF only
- Automatic file cleanup after processing
- No persistent storage

## 📋 API Endpoints

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

## 🔍 Testing

### Test Individual PDFs
```bash
python test_parser.py path/to/statement.pdf
```

### Test All Sample Files
```bash
# Test all sample PDFs
for file in sample/*.pdf; do
    python test_parser.py "$file"
done
```

## 🐛 Troubleshooting

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
FLASK_DEBUG=1 python app.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔐 Security Notice

- **Local Processing**: All PDF parsing happens on your local machine
- **No Data Storage**: Files are automatically deleted after processing
- **Privacy First**: Your financial data never leaves your control
- **Open Source**: Full source code available for security review

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the test files for examples

## 🎯 Roadmap

- [ ] OCR support for scanned PDFs
- [ ] Additional bank support
- [ ] Batch processing
- [ ] Advanced analytics
- [ ] Mobile app
- [ ] API rate limiting
- [ ] User authentication

---

**⚠️ Important**: This tool processes sensitive financial documents. Always ensure you're running the latest version and review the code before use. For maximum security, run the backend locally and never store parsed data on external servers.
