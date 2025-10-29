import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from Trust_Analysis import TrustAnalysis


class HTMLLinkScanner:
    """
    HTML Link Scanner for detecting potential scams in web pages
    Extracts all <a> elements and analyzes their URLs for legitimacy
    """
    
    def __init__(self):
        self.trust_analyzer = TrustAnalysis()
    
    def extract_links_from_html(self, html_content, base_url=None):
        """
        Extract all <a> elements with their href URLs and text from HTML content
        
        Args:
            html_content (str): The HTML content to parse
            base_url (str, optional): Base URL for resolving relative URLs
            
        Returns:
            list: List of dictionaries containing link information
        """
        links = []
        
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            anchor_tags = soup.find_all('a', href=True)
            
            for anchor in anchor_tags:
                href = anchor.get('href', '')
                text = anchor.get_text(strip=True) or href
                
                # Resolve relative URLs
                if base_url and not href.startswith(('http://', 'https://')):
                    href = urljoin(base_url, href)
                
                link_info = {
                    'url': href,
                    'text': text,
                    'html': str(anchor)
                }
                links.append(link_info)
        
        except Exception as e:
            print(f"Error parsing HTML: {str(e)}")
            # Fallback to regex if BeautifulSoup fails
            return self._extract_links_with_regex(html_content, base_url)
        
        return links
    
    def _extract_links_with_regex(self, html_content, base_url=None):
        """
        Fallback method using regex to extract links from HTML
        
        Args:
            html_content (str): The HTML content
            base_url (str, optional): Base URL for resolving relative URLs
            
        Returns:
            list: List of dictionaries containing link information
        """
        links = []
        # Regex to find <a> tags with href attributes
        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html_content, re.IGNORECASE | re.DOTALL)
        
        for match in matches:
            href, text = match
            text = re.sub(r'<[^>]+>', '', text).strip()
            
            # Resolve relative URLs
            if base_url and not href.startswith(('http://', 'https://')):
                href = urljoin(base_url, href)
            
            links.append({
                'url': href,
                'text': text or href,
                'html': f'<a href="{href}">{text}</a>'
            })
        
        return links
    
    def scan_links(self, html_content, base_url=None):
        """
        Scan all links in HTML content and analyze them for scams
        
        Args:
            html_content (str): The HTML content to scan
            base_url (str, optional): Base URL for resolving relative URLs
            
        Returns:
            dict: Comprehensive scan results with all analyzed links
        """
        links = self.extract_links_from_html(html_content, base_url)
        
        scan_results = {
            'total_links': len(links),
            'trusted_links': [],
            'suspicious_links': [],
            'likely_scam_links': [],
            'all_links_analysis': []
        }
        
        for idx, link in enumerate(links, 1):
            url = link.get('url', '')
            text = link.get('text', '')
            
            if not url:
                continue
            
            # Analyze the URL
            analysis = self.trust_analyzer.analyze_url(url)
            analysis['link_text'] = text
            analysis['link_index'] = idx
            
            scan_results['all_links_analysis'].append(analysis)
            
            # Categorize the link
            trust_score = analysis.get('trust_score', 0)
            
            if trust_score >= 80:
                scan_results['trusted_links'].append({
                    'url': url,
                    'text': text,
                    'trust_score': trust_score,
                    'status': analysis.get('status', 'Unknown')
                })
            elif trust_score >= 50:
                scan_results['suspicious_links'].append({
                    'url': url,
                    'text': text,
                    'trust_score': trust_score,
                    'status': analysis.get('status', 'Unknown'),
                    'risk_indicators': analysis.get('risk_indicators', 0)
                })
            else:
                scan_results['likely_scam_links'].append({
                    'url': url,
                    'text': text,
                    'trust_score': trust_score,
                    'status': analysis.get('status', 'Unknown'),
                    'risk_indicators': analysis.get('risk_indicators', 0),
                    'details': analysis.get('details', [])
                })
        
        # Calculate overall page safety score
        if scan_results['total_links'] > 0:
            safe_ratio = len(scan_results['trusted_links']) / scan_results['total_links']
            scam_ratio = len(scan_results['likely_scam_links']) / scan_results['total_links']
            scan_results['overall_safety_score'] = int((safe_ratio * 100) - (scam_ratio * 50))
            
            if scam_ratio > 0.5:
                scan_results['page_verdict'] = "LIKELY SCAM SITE"
            elif scam_ratio > 0.2:
                scan_results['page_verdict'] = "CAUTION - Contains suspicious links"
            elif safe_ratio > 0.7:
                scan_results['page_verdict'] = "LIKELY SAFE"
            else:
                scan_results['page_verdict'] = "NEEDS REVIEW"
        else:
            scan_results['overall_safety_score'] = 0
            scan_results['page_verdict'] = "NO LINKS FOUND"
        
        return scan_results
    
    def scan_html_file(self, file_path):
        """
        Scan links from an HTML file
        
        Args:
            file_path (str): Path to the HTML file
            
        Returns:
            dict: Scan results
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            return self.scan_links(html_content)
        
        except FileNotFoundError:
            return {
                'error': f"File not found: {file_path}"
            }
        except Exception as e:
            return {
                'error': f"Error reading file: {str(e)}"
            }
    
    def scan_url(self, url):
        """
        Fetch HTML from URL and scan links (requires requests library)
        
        Args:
            url (str): The URL to scan
            
        Returns:
            dict: Scan results
        """
        try:
            import requests
            from urllib.parse import urlparse
            
            response = requests.get(url, timeout=10, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            response.raise_for_status()
            html_content = response.text
            
            return self.scan_links(html_content, base_url=url)
        
        except ImportError:
            return {
                'error': "requests library not installed. Install with: pip install requests"
            }
        except Exception as e:
            return {
                'error': f"Error fetching URL: {str(e)}"
            }
    
    def generate_report(self, scan_results):
        """
        Generate a human-readable report from scan results
        
        Args:
            scan_results (dict): Results from scan_links()
            
        Returns:
            str: Formatted report
        """
        report = []
        report.append("=" * 60)
        report.append("HTML LINK SCAN REPORT")
        report.append("=" * 60)
        report.append("")
        
        if 'error' in scan_results:
            report.append(f"ERROR: {scan_results['error']}")
            return "\n".join(report)
        
        report.append(f"Total Links Found: {scan_results['total_links']}")
        report.append(f"Overall Safety Score: {scan_results.get('overall_safety_score', 0)}/100")
        report.append(f"Page Verdict: {scan_results.get('page_verdict', 'UNKNOWN')}")
        report.append("")
        
        # Trusted links
        if scan_results['trusted_links']:
            report.append("-" * 60)
            report.append(f"TRUSTED LINKS ({len(scan_results['trusted_links'])}):")
            report.append("-" * 60)
            for link in scan_results['trusted_links']:
                report.append(f"  ✓ {link['url']}")
                report.append(f"    Text: {link['text']}")
                report.append(f"    Trust Score: {link['trust_score']}")
                report.append("")
        
        # Suspicious links
        if scan_results['suspicious_links']:
            report.append("-" * 60)
            report.append(f"SUSPICIOUS LINKS ({len(scan_results['suspicious_links'])}):")
            report.append("-" * 60)
            for link in scan_results['suspicious_links']:
                report.append(f"  ⚠ {link['url']}")
                report.append(f"    Text: {link['text']}")
                report.append(f"    Trust Score: {link['trust_score']}")
                report.append(f"    Risk Indicators: {link['risk_indicators']}")
                report.append("")
        
        # Likely scam links
        if scan_results['likely_scam_links']:
            report.append("-" * 60)
            report.append(f"LIKELY SCAM LINKS ({len(scan_results['likely_scam_links'])}):")
            report.append("-" * 60)
            for link in scan_results['likely_scam_links']:
                report.append(f"  ✗ SCAM: {link['url']}")
                report.append(f"    Text: {link['text']}")
                report.append(f"    Trust Score: {link['trust_score']}")
                report.append(f"    Details:")
                for detail in link.get('details', []):
                    report.append(f"      - {detail}")
                report.append("")
        
        report.append("=" * 60)
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    scanner = HTMLLinkScanner()
    
    # Example: Scan HTML from a string
    sample_html = """
    <html>
    <body>
        <h1>Example Page</h1>
        <a href="https://www.google.com">Safe Link</a>
        <a href="https://example.com">Another Safe Link</a>
        <a href="https://suspicious-site-free-prize-winner.xyz/tk/claim">Suspicious Link</a>
        <a href="http://unsecured-website.com/payment">Unsecured Site</a>
    </body>
    </html>
    """
    
    results = scanner.scan_links(sample_html)
    report = scanner.generate_report(results)
    print(report)

