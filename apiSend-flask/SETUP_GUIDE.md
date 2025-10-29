# Setup Guide for HTML Link Scanner

## Quick Start

1. **Install Dependencies**

```bash
cd "apiSend-flask"
pip install -r requirements.txt
```

2. **Test the Scanner**

```bash
python HTML_Link_Scanner.py
```

3. **Run the Demo**

```bash
python demo_link_scanner.py
```

4. **Start the Flask API**

```bash
python app.py
```

## What's New

### Enhanced Files

- ✅ **Trust_Analysis.py** - Now includes comprehensive scam detection:
  - Suspicious keyword detection
  - TLD reputation analysis
  - Typo squatting detection
  - Homograph attack detection
  - URL length analysis
  - HTTPS validation
  - Domain pattern analysis

### New Files

- ✅ **HTML_Link_Scanner.py** - Extracts and analyzes all links from HTML:

  - Finds all `<a>` elements
  - Categorizes links as Trusted/Suspicious/Scam
  - Generates detailed reports
  - Supports files, HTML strings, and live URLs

- ✅ **demo_link_scanner.py** - Example usage demonstrations

- ✅ **requirements.txt** - All necessary dependencies

- ✅ **README_LINK_SCANNER.md** - Comprehensive documentation

### Updated Files

- ✅ **app.py** - Added new Flask endpoints:
  - `/scan-links` - Scan links from HTML or URL
  - `/scan-links-file` - Upload HTML file for scanning

## API Usage

### Analyze Single URL

```bash
POST http://localhost:5000/analyze
{
  "url": "https://example.com"
}
```

### Scan Links from HTML

```bash
POST http://localhost:5000/scan-links
{
  "html": "<html><body><a href='url'>Link</a></body></html>",
  "base_url": "https://example.com"
}
```

### Scan Links from Live URL

```bash
POST http://localhost:5000/scan-links
{
  "url": "https://website-to-scan.com"
}
```

### Upload HTML File

```bash
POST http://localhost:5000/scan-links-file
Content-Type: multipart/form-data
file: @webpage.html
```

## Integration Example

### Python Script

```python
from HTML_Link_Scanner import HTMLLinkScanner

scanner = HTMLLinkScanner()
results = scanner.scan_url("https://example-site.com")

print(f"Safety Score: {results['overall_safety_score']}")
print(f"Verdict: {results['page_verdict']}")

for scam_link in results['likely_scam_links']:
    print(f"⚠ SCAM: {scam_link['url']}")
```

### JavaScript/AJAX

```javascript
fetch("http://localhost:5000/scan-links", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    html: document.documentElement.outerHTML,
    base_url: window.location.href,
  }),
})
  .then((r) => r.json())
  .then((results) => {
    console.log("Verdict:", results.page_verdict);
    console.log("Scam links:", results.likely_scam_links);
  });
```

## Testing

Run the demo script to see all features in action:

```bash
python demo_link_scanner.py
```

Expected output includes:

- Sample HTML link scanning
- Individual URL trust analysis
- File-based scanning
- Batch URL analysis
