from urllib.parse import urlparse
import re
from Domain_Check import DomainCheck


class TrustAnalysis:
    """
    Trust analysis class for URL analysis with scam detection
    """
    
    # Suspicious keywords often used in scam URLs
    SUSPICIOUS_KEYWORDS = [
        'free', 'prize', 'winner', 'urgent', 'limited', 'click', 'verify',
        'account', 'suspended', 'update', 'confirm', 'security', 'alert',
        'bank', 'payment', 'refund', 'congratulations', 'claim', 'offer'
    ]
    
    # Common TLDs used in phishing/scams
    SUSPICIOUS_TLDS = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.click']
    
    # Suspicious subdomains
    SUSPICIOUS_SUBDOMAINS = ['secure', 'verify', 'update', 'login', 'account']
    
    def __init__(self):
        self.domain_analyzer = None
    
    def _extract_domain(self, url):
        """
        Extract domain from URL
        
        Args:
            url (str): The URL to parse
            
        Returns:
            str: Extracted domain or empty string
        """
        try:
            parsed = urlparse(url)
            domain = parsed.netloc or parsed.path
            # Remove port if present
            domain = domain.split(':')[0]
            return domain
        except Exception:
            return ""
    
    def _check_url_length(self, url):
        """
        Check if URL is suspiciously long (often used to hide real domain)
        
        Returns:
            bool: True if URL is suspiciously long
        """
        return len(url) > 200
    
    def _check_suspicious_keywords(self, url):
        """
        Check for suspicious keywords in URL
        
        Returns:
            int: Number of suspicious keywords found
        """
        url_lower = url.lower()
        count = sum(1 for keyword in self.SUSPICIOUS_KEYWORDS if keyword in url_lower)
        return count
    
    def _check_typo_squatting(self, domain):
        """
        Basic check for potential typo squatting patterns
        
        Returns:
            bool: True if potential typo squatting detected
        """
        # Check for common typos
        common_typos = [
            ('o', '0'), ('i', '1'), ('l', '1'), 
            ('m', 'rn'), ('w', 'vv'), ('g', 'q')
        ]
        domain_lower = domain.lower()
        for original, typo in common_typos:
            if typo in domain_lower and original not in domain_lower:
                return True
        return False
    
    def _check_mixed_content(self, url):
        """
        Check for suspicious character usage (IDN homograph attacks)
        
        Returns:
            bool: True if mixed/alphanumeric characters detected
        """
        # Check for non-ASCII characters that could be used in homograph attacks
        return bool(re.search(r'[^\x00-\x7F]', url)) or bool(re.search(r'[а-яё]', url))
    
    def _check_https(self, url):
        """
        Check if URL uses HTTPS
        
        Returns:
            bool: True if HTTPS is used
        """
        return url.startswith('https://')
    
    def _check_domain_age_pattern(self, domain):
        """
        Check for suspicious domain patterns (long random strings)
        
        Returns:
            bool: True if domain looks like random string
        """
        parts = domain.split('.')
        if len(parts) >= 2:
            # Check if domain name is very long (likely random)
            domain_name = parts[0]
            if len(domain_name) > 20 and not domain_name.replace('-', '').isalnum():
                return True
        return False
    
    def analyze_url(self, url):
        """
        Analyze a URL and return comprehensive trust analysis results
        
        Args:
            url (str): The URL to analyze
            
        Returns:
            dict: Analysis results with trust score, status, and detailed analysis
        """
        if not url or not isinstance(url, str):
            return {
                "url": url,
                "trust_score": 0,
                "status": "Invalid URL",
                "details": []
            }
        
        domain = self._extract_domain(url)
        details = []
        risk_score = 0  # 0 = safe, 100 = high risk
        
        # Initialize domain checker
        if domain:
            self.domain_analyzer = DomainCheck(domain)
            domain_info = self.domain_analyzer.to_dict()
            
            # Full trusted domains get high trust score
            if domain_info.get('full_trusted'):
                trust_score = 95
                status = "Trusted"
                details.append("Domain is in trusted registry (.bn or .com)")
            # Partial trusted domains get medium score
            elif domain_info.get('partial_trusted'):
                trust_score = 75
                status = "Likely Safe"
                details.append("Domain is in partially trusted registry (.gov, .edu)")
            else:
                # Analyze for scams
                trust_score = 60
                status = "Needs Review"
                details.append("Domain not in trusted registries")
        else:
            trust_score = 0
            status = "Invalid"
            details.append("Could not extract domain from URL")
        
        # Check URL length
        if self._check_url_length(url):
            risk_score += 30
            details.append("URL is suspiciously long (possible redirect hiding)")
        
        # Check for suspicious keywords
        keyword_count = self._check_suspicious_keywords(url)
        if keyword_count > 0:
            risk_score += keyword_count * 5
            details.append(f"Found {keyword_count} suspicious keyword(s) in URL")
        
        # Check domain for issues
        if domain:
            # Check for suspicious TLD
            if any(tld in domain for tld in self.SUSPICIOUS_TLDS):
                risk_score += 20
                details.append("Domain uses suspicious TLD")
            
            # Check for typo squatting
            if self._check_typo_squatting(domain):
                risk_score += 25
                details.append("Potential typo squatting detected")
            
            # Check for mixed content/homograph attacks
            if self._check_mixed_content(domain):
                risk_score += 30
                details.append("Suspicious characters detected (possible homograph attack)")
            
            # Check for random-looking domain
            if self._check_domain_age_pattern(domain):
                risk_score += 15
                details.append("Domain appears to be randomly generated")
        
        # HTTPS check
        if self._check_https(url):
            details.append("✓ Uses HTTPS")
        else:
            risk_score += 10
            details.append("✗ Does not use HTTPS")
        
        # Adjust trust score based on risk
        final_trust_score = max(0, min(100, trust_score - risk_score))
        
        # Determine final status
        if final_trust_score >= 80:
            final_status = "Trusted"
        elif final_trust_score >= 60:
            final_status = "Likely Safe"
        elif final_trust_score >= 40:
            final_status = "Caution"
        else:
            final_status = "Likely Scam"
        
        result = {
            "url": url,
            "trust_score": final_trust_score,
            "status": final_status,
            "domain": domain,
            "details": details,
            "risk_indicators": len([d for d in details if any(word in d.lower() for word in ['suspicious', 'potential', 'does not', 'randomly'])])
        }
        
        return result
    
    def get_trust_score(self, url):
        """
        Get only the trust score for a URL
        
        Args:
            url (str): The URL to analyze
            
        Returns:
            int: Trust score (0-100)
        """
        analysis = self.analyze_url(url)
        return analysis.get("trust_score", 0)
    
    def get_status(self, url):
        """
        Get only the status for a URL
        
        Args:
            url (str): The URL to analyze
            
        Returns:
            str: Status message
        """
        analysis = self.analyze_url(url)
        return analysis.get("status", "Unknown")
    
    def is_likely_scam(self, url):
        """
        Quick check if URL is likely a scam
        
        Args:
            url (str): The URL to check
            
        Returns:
            bool: True if likely a scam, False otherwise
        """
        analysis = self.analyze_url(url)
        return analysis.get("trust_score", 50) < 50 or analysis.get("status", "").lower() in ["likely scam", "caution"]
