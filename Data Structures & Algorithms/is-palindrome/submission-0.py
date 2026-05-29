class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_str = [ch.lower() for ch in s if ch.isalnum()]
        return strip_str == strip_str[::-1]
        