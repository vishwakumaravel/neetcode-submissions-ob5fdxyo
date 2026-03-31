class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = ''
        for char in s:
            if char.isalnum():
                stri += char

        stri_lower = stri.lower()
        if stri_lower == stri_lower[::-1]:
            return True
        else:
            return False
