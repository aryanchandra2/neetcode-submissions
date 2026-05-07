class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list)
        for s in strs:
            characters = [0] * 26
            for c in s:
                characters[ord(c) - ord('a')] += 1
            hashtable[tuple(characters)].append(s)
        return list(hashtable.values())

