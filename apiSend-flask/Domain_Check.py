class DomainCheck:
    FULL_TRUST_SUFFIXES = [".bn"]  # Brunei domains
    PARTIAL_TRUST_SUFFIXES = [".gov", ".edu"]  # Recognized but not necessarily Brunei

    def __init__(self, domain: str):
        self.domain = domain.lower().strip()
        self.valid = self._is_valid()
        self.full_trusted = self._is_full_trusted() if self.valid else False
        self.partial_trusted = self._is_partial_trusted() if self.valid and not self.full_trusted else False

    def _is_valid(self) -> bool:
        """
        Basic validation: must contain at least one dot, not empty, and reasonable length.
        """
        return bool(self.domain) and '.' in self.domain and len(self.domain) > 3

    def _is_full_trusted(self) -> bool:
        """
        Full trust if domain ends with .bn (including subdomains like .gov.bn, .edu.bn)
        """
        return any(self.domain.endswith(suffix) for suffix in self.FULL_TRUST_SUFFIXES)

    def _is_partial_trusted(self) -> bool:
        """
        Partial trust if domain ends with recognized suffixes but not .bn
        """
        return any(self.domain.endswith(suffix) for suffix in self.PARTIAL_TRUST_SUFFIXES) and not self.full_trusted

    def to_dict(self) -> dict:
        return {
            "domain": self.domain,
            "valid": self.valid,
            "full_trusted": self.full_trusted,
            "partial_trusted": self.partial_trusted
        }
