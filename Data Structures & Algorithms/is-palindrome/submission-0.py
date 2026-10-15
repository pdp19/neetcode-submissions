class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
        