class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for i in range(len(strs)):
            anagramDict["".join(sorted(strs[i]))].append(strs[i])
        
        return list(anagramDict.values())
        