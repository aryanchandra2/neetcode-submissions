class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = [-1,-1]
        minWindow = float("inf")
        need = 0
        have = 0
        freqT = defaultdict(int)
        freqWindow = defaultdict(int)

        for i in range(len(t)):
            freqT[t[i]] += 1
        
        need = len(freqT)
        for r in range(len(s)):
            freqWindow[s[r]] += 1
            if s[r] in freqT and freqWindow[s[r]] == freqT[s[r]]:
                have += 1
            while have == need:
                
                
                if r - l + 1 < minWindow:
                    minWindow = r - l + 1
                    res = [l, r + 1]
                
                if s[l] in freqT and freqWindow[s[l]] == freqT[s[l]]:
                    have -= 1
                freqWindow[s[l]] -= 1 
                l += 1
        if minWindow == float("inf"):
            return ""
        return s[res[0] : res[1]]