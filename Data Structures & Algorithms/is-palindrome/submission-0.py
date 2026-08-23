class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        reverse = ""

        for char in reversed(cleaned):
            reverse += char
        

        return reverse == cleaned

        