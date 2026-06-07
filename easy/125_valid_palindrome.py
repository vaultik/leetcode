import re


# My solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = (re.sub(r'[\W\s_]', '', s)).lower()
        return clean_text == clean_text[::-1]


# Cleaner version – explicit allowlist [^a-z0-9]
class SolutionClean:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-z0-9]', '', s.lower())
        return clean == clean[::-1]
