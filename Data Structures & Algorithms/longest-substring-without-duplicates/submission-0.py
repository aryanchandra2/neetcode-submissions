class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # last left indexes
        leftIndex = 0
        result = 0

        for r in range(len(s)):
            if s[r] in mp:
                leftIndex = max(mp[s[r]] + 1, leftIndex)
            mp[s[r]] = r
            result = max(result, r - leftIndex + 1)
        
        return result





