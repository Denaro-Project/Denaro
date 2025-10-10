from flask import Flask, request, jsonify
from Trust_Analysis import TrustAnalysis
from Domain_Check import DomainCheck

# from urllib.parse import urlparse

import tldextract


app = Flask(__name__)

# Initialize the trust analysis instance
trust_analyzer = TrustAnalysis()

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

if __name__ == '__main__':
    app.run(port=5000, debug=True)


