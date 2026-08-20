class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mp = defaultdict(int)
        ret = 0
        maxCharFreq = 0 #keep track of which character is most frequent
        for r in range(len(s)):
            mp[s[r]] += 1
            maxCharFreq = max(maxCharFreq, mp[s[r]])
            if r - l + 1 - maxCharFreq > k:
                mp[s[l]] -= 1
                l += 1
            ret = max(r - l + 1, ret)
        return ret
