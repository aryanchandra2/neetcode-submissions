class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ret = 0
        maxFreq = 0
        windowFreqs = defaultdict(int)
        for r in range(len(s)):
            windowFreqs[s[r]] += 1
            maxFreq = max(maxFreq, windowFreqs[s[r]])
            if (r - l + 1) - maxFreq > k:
                windowFreqs[s[l]] -= 1
                l += 1
            ret = max(r - l + 1, ret)
        return ret




