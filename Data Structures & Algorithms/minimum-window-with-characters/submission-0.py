class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, minLen = 0, float("inf")
        window, chars = defaultdict(int), defaultdict(int)
        have = 0
        for i in t:
            chars[i] += 1
        result = [-1,-1]
        need = len(chars)
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == chars[s[r]]:
                have += 1
                

            while have == need:
                if (r - l + 1) < minLen: 
                    minLen = r - l + 1
                    result = [l, r]
                
                window[s[l]] -= 1
                if s[l] in chars and window[s[l]] < chars[s[l]]:
                    have -=1
                l += 1

                
        l, r = result
        return s[l : r+1] if minLen != float("inf") else ""