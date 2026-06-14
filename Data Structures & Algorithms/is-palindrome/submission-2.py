class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not self.alphaNum(s[i]):
                i += 1
                continue
            if not self.alphaNum(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True

    def alphaNum(self, c) -> bool:
        i = ord(c)
        return (i >= ord('a') and i <= ord('z')) or (i >= ord('0') and i <= ord('9')) or (i >= ord('A') and i <= ord('Z'))