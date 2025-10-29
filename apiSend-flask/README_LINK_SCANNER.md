# HTML Link Scanner & Trust Analysis

A comprehensive Python toolset for detecting scam links in web pages by analyzing URLs for trustworthiness and security indicators.

## Features

### Trust_Analysis.py

Enhanced with comprehensive scam detection:

- **Domain validation** using trusted registries (.bn, .com, .gov, .edu)
- **Suspicious keyword detection** (free, prize, urgent, verify, etc.)
- **Suspicious TLD detection** (.tk, .ml, .ga, .xyz, etc.)
- **Typo squatting detection**
- **IDN homograph attack detection**
- **HTTPS validation**
- **URL length analysis** (long URLs often hide redirects)
- **Domain pattern analysis** (detecting randomly generated domains)

### HTML_Link_Scanner.py

Scans HTML pages and analyzes all links:

- Extracts all `<a>` elements from HTML
- Resolves relative URLs with base URL support
- Categorizes links: Trusted, Suspicious, or Likely Scam
- Generates comprehensive reports with risk indicators
- Supports HTML files, HTML strings, and live URLs

## Installation

1. Install required packages:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install Flask beautifulsoup4 requests tldextract
```

## Usage

### Basic Usage - Trust Analysis

```python
from Trust_Analysis import TrustAnalysis

# Initialize analyzer
analyzer = TrustAnalysis()

# Analyze a URL
result = analyzer.analyze_url("https://example.com")

print(f"Trust Score: {result['trust_score']}")
print(f"Status: {result['status']}")
print(f"Details: {result['details']}")

# Quick scam check
is_scam = analyzer.is_likely_scam("https://suspicious-site.xyz")
```

### HTML Link Scanner

#### Scan HTML Content

```python
from HTML_Link_Scanner import HTMLLinkScanner

# Initialize scanner
scanner = HTMLLinkScanner()

# Scan HTML string
html = """
<html>
<body>
    <a href="https://www.google.com">Google</a>
    <a href="https://free-prize.tk/claim">Suspicious Link</a>
</body>
</html>
"""

results = scanner.scan_links(html)

# Generate report
report = scanner.generate_report(results)
print(report)
```

#### Scan HTML File

```python
# Scan from file
results = scanner.scan_html_file("webpage.html")
print(scanner.generate_report(results))
```

#### Scan Live URL

```python
# Fetch and scan a live URL
results = scanner.scan_url("https://example-website.com")
print(scanner.generate_report(results))
```

### Flask API Endpoints

#### 1. `/analyze` - Analyze Single URL

```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

#### 2. `/scan-links` - Scan Links from HTML or URL

**Scan HTML content:**

```bash
curl -X POST http://localhost:5000/scan-links \
  -H "Content-Type: application/json" \
  -d '{
    "html": "<html><body><a href=\"https://example.com\">Link</a></body></html>",
    "base_url": "https://example.com"
  }'
```

**Scan from URL:**

```bash
curl -X POST http://localhost:5000/scan-links \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example-website.com"}'
```

#### 3. `/scan-links-file` - Upload HTML File

```bash
curl -X POST http://localhost:5000/scan-links-file \
  -F "file=@webpage.html"
```

## Output Format

### Trust Analysis Output

```json
{
  "url": "https://example.com",
  "trust_score": 75,
  "status": "Likely Safe",
  "domain": "example.com",
  "details": ["Domain not in trusted registries", "✓ Uses HTTPS"],
  "risk_indicators": 0
}
```

### Link Scanner Output

```json
{
  "total_links": 5,
  "trusted_links": [...],
  "suspicious_links": [...],
  "likely_scam_links": [...],
  "overall_safety_score": 60,
  "page_verdict": "LIKELY SAFE"
}
```

## Trust Score Ranges

- **80-100**: Trusted
- **60-79**: Likely Safe
- **40-59**: Caution
- **0-39**: Likely Scam

## Detected Scam Indicators

The system detects various scam patterns:

1. **Suspicious Keywords**: free, prize, winner, urgent, verify, claim
2. **Suspicious TLDs**: .tk, .ml, .ga, .cf, .gq, .xyz
3. **Long URLs**: Over 200 characters (hiding redirect chains)
4. **No HTTPS**: Insecure connections
5. **Typo Squatting**: Character substitutions (0 for O, 1 for I)
6. **Homograph Attacks**: Non-ASCII characters resembling letters
7. **Random Domains**: Suspiciously long, random-looking subdomains
8. **Untrusted Registries**: Domains not in trusted registries

## Running the Demo

```bash
cd apiSend-flask
python demo_link_scanner.py
```

This will run comprehensive demos showing:

- Basic link scanning
- Individual URL trust analysis
- HTML file scanning
- Batch URL analysis

## Examples

### Example 1: Basic Scam Detection

```python
from Trust_Analysis import TrustAnalysis

analyzer = TrustAnalysis()

# Check if URL is likely a scam
url = "https://free-bitcoin-claim.xyz/tk/winner"
is_scam = analyzer.is_likely_scam(url)
print(f"Is scam: {is_scam}")  # True

# Get detailed analysis
result = analyzer.analyze_url(url)
print(result['status'])  # "Likely Scam"
```

### Example 2: Scan Webpage for Malicious Links

```python
from HTML_Link_Scanner import HTMLLinkScanner

scanner = HTMLLinkScanner()

# Analyze a webpage
results = scanner.scan_url("https://example-site.com")

# Check for scam links
if results['likely_scam_links']:
    print(f"Found {len(results['likely_scam_links'])} potential scam links!")
    for link in results['likely_scam_links']:
        print(f"  - {link['url']}")
```

### Example 3: Batch URL Checking

```python
urls = [
    "https://www.google.com",
    "https://suspicious-free.ml/claim",
    "https://secure-login.bank.tk"
]

for url in urls:
    result = analyzer.analyze_url(url)
    print(f"{url}: {result['status']} (Score: {result['trust_score']})")
```

## File Structure

```
apiSend-flask/
├── Trust_Analysis.py          # Enhanced trust analysis with scam detection
├── HTML_Link_Scanner.py       # HTML link extraction and scanning
├── Domain_Check.py            # Domain registry validation
├── app.py                     # Flask API with new endpoints
├── demo_link_scanner.py       # Comprehensive demo script
├── requirements.txt           # Python dependencies
└── README_LINK_SCANNER.md    # This file
```

## Security Notes

- Always validate user input before processing
- Consider rate limiting for API endpoints
- Use HTTPS in production
- The tool provides guidance but should be used alongside other security measures
- Some false positives may occur; review results before taking action

## Integration with Laravel Webapp

The Flask API can be integrated with your Laravel application:

```php
// In Laravel
$response = Http::post('http://localhost:5000/scan-links', [
    'url' => $request->input('url')
]);

$results = $response->json();

if ($results['page_verdict'] === 'LIKELY SCAM SITE') {
    // Handle suspicious site
}
```

## License

This tool is part of the Denaro Project.
