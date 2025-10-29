"""
Demo script for HTML Link Scanner
Shows how to use the HTMLLinkScanner to detect scam links in web pages
"""

from HTML_Link_Scanner import HTMLLinkScanner
from Trust_Analysis import TrustAnalysis


def demo_basic_scan():
    """Demo 1: Basic link scanning from HTML string"""
    print("\n" + "="*70)
    print("DEMO 1: Basic HTML Link Scanning")
    print("="*70)
    
    scanner = HTMLLinkScanner()
    
    # Sample HTML with various types of links
    sample_html = """
    <html>
    <body>
        <h1>Sample Web Page</h1>
        <p>Here are some links:</p>
        <ul>
            <li><a href="https://www.google.com">Google - Trusted Search</a></li>
            <li><a href="https://www.example.com">Example Website</a></li>
            <li><a href="https://secure-account-verify-refund-free.tk/claim">Claim Your Prize</a></li>
            <li><a href="http://unsecured-payment.bank.com">Bank Login</a></li>
            <li><a href="https://suspicious-free-xml.xyz/urgent">Urgent: Update Required</a></li>
            <li><a href="https://www.github.com">GitHub - Developer Platform</a></li>
        </ul>
    </body>
    </html>
    """
    
    results = scanner.scan_links(sample_html)
    report = scanner.generate_report(results)
    print(report)


def demo_trust_analysis():
    """Demo 2: Individual URL trust analysis"""
    print("\n" + "="*70)
    print("DEMO 2: Individual URL Trust Analysis")
    print("="*70)
    
    analyzer = TrustAnalysis()
    
    test_urls = [
        "https://www.google.com",
        "https://free-prize-winner.claim.tk/verify",
        "https://secure-payment.bank.com/login",
        "https://example.com.gov.bn",
        "https://suspicious-site.xyz/update?redirect=http://evil.com"
    ]
    
    for url in test_urls:
        analysis = analyzer.analyze_url(url)
        print(f"\nURL: {url}")
        print(f"Trust Score: {analysis['trust_score']}/100")
        print(f"Status: {analysis['status']}")
        print(f"Domain: {analysis.get('domain', 'Unknown')}")
        print(f"Risk Indicators: {analysis.get('risk_indicators', 0)}")
        
        if analysis.get('details'):
            print("Details:")
            for detail in analysis['details']:
                print(f"  - {detail}")
        
        is_scam = analyzer.is_likely_scam(url)
        print(f"Is Likely Scam: {'YES' if is_scam else 'NO'}")


def demo_file_scan():
    """Demo 3: Scan HTML file"""
    print("\n" + "="*70)
    print("DEMO 3: Scan HTML File")
    print("="*70)
    
    scanner = HTMLLinkScanner()
    
    # Create a sample HTML file
    sample_html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>Click on the links below:</p>
    <a href="https://www.linkedin.com">Professional Network</a><br>
    <a href="https://malicious-tracking-free.ml/track">Free Downloads</a><br>
    <a href="https://www.wikipedia.org">Knowledge Base</a><br>
    <a href="http://bank-secure-login-update.com/verify">Bank Verification</a><br>
</body>
</html>"""
    
    # Write to a temporary file
    with open('temp_sample.html', 'w', encoding='utf-8') as f:
        f.write(sample_html_content)
    
    print("Scanning temp_sample.html...")
    results = scanner.scan_html_file('temp_sample.html')
    report = scanner.generate_report(results)
    print(report)
    
    # Cleanup
    import os
    if os.path.exists('temp_sample.html'):
        os.remove('temp_sample.html')
        print("\n(Temp file removed)")


def demo_batch_analysis():
    """Demo 4: Batch URL analysis"""
    print("\n" + "="*70)
    print("DEMO 4: Batch URL Analysis")
    print("="*70)
    
    analyzer = TrustAnalysis()
    
    urls_to_check = [
        "https://www.amazon.com",
        "https://www.microsoft.com",
        "https://free-bitcoin-claim.xyz/tk/winner",
        "https://urgent-secure-account.ml/update",
        "https://www.unicef.org",
        "https://suspicious-offer12345.click/free"
    ]
    
    print("\nBatch Analysis Results:\n")
    print(f"{'URL':<50} {'Score':<8} {'Status':<15} {'Scam?'}")
    print("-" * 90)
    
    for url in urls_to_check:
        analysis = analyzer.analyze_url(url)
        is_scam = analyzer.is_likely_scam(url)
        scam_indicator = "⚠ YES" if is_scam else "✓ NO"
        
        print(f"{url[:48]:<50} {analysis['trust_score']:<8} {analysis['status']:<15} {scam_indicator}")
    
    print("\n" + "="*90)


def main():
    """Run all demos"""
    print("\n" + "="*70)
    print("HTML LINK SCANNER & TRUST ANALYSIS - DEMONSTRATION")
    print("="*70)
    
    try:
        demo_basic_scan()
        demo_trust_analysis()
        demo_file_scan()
        demo_batch_analysis()
        
        print("\n" + "="*70)
        print("ALL DEMOS COMPLETED")
        print("="*70)
        
    except Exception as e:
        print(f"\nError during demo: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

