from flask import Flask, request, jsonify
from Trust_Analysis import TrustAnalysis
from Domain_Check import DomainCheck
from HTML_Link_Scanner import HTMLLinkScanner

# from urllib.parse import urlparse

import tldextract


app = Flask(__name__)

# Initialize the trust analysis instance
trust_analyzer = TrustAnalysis()
html_scanner = HTMLLinkScanner()

@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url  # temporary scheme for parsing
    return url

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    # print("Received data:", data)
    # url = data.get("url") or ""
    url = normalize_url(data["url"])

    # Extract domain
    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}" if ext.domain and ext.suffix else ""

    # Run Trust Analysis
    trust_result = trust_analyzer.analyze_url(url)

    # Run Domain Check safely
    checker = DomainCheck(domain)
    domain_result = checker.to_dict()

    # Merge results
    result = {
        **trust_result,
        "domain_check": domain_result
    }

    return jsonify(result)
    # return "Hello World"


@app.route('/scan-links', methods=['POST'])
def scan_links():
    """
    Scan links from HTML content or URL
    Accepts:
    - 'html': HTML content string
    - 'url': URL to fetch and scan
    - 'base_url': Optional base URL for relative links
    """
    try:
        data = request.json
        
        if 'html' in data:
            # Scan HTML content
            html_content = data.get('html', '')
            base_url = data.get('base_url', None)
            results = html_scanner.scan_links(html_content, base_url)
            
        elif 'url' in data:
            # Fetch and scan URL
            url = normalize_url(data['url'])
            results = html_scanner.scan_url(url)
            
        else:
            return jsonify({
                'error': 'Either "html" or "url" must be provided'
            }), 400
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/scan-links-file', methods=['POST'])
def scan_links_file():
    """
    Scan links from an uploaded HTML file
    """
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read file content
        html_content = file.read().decode('utf-8')
        
        # Scan links
        results = html_scanner.scan_links(html_content)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)


