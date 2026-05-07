class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for i in range(len(strs)):
            key = [0] * 26
            for j in strs[i]:
                key[ord(j) - ord('a')] += 1
            anagramDict[tuple(key)].append(strs[i])
            
        return list(anagramDict.values())
        