class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS, hashT = {}, {}
        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
        for i in range(len(t)):
            hashT[t[i]] = hashT.get(t[i], 0) + 1
        return hashS == hashT