class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        array1, array2 = [0] * 26, [0] * 26
        for s in range(len(s1)):
            array1[ord(s1[s]) - ord('a')] += 1
            array2[ord(s2[s]) - ord('a')] += 1
        
        if array1 == array2:
            return True

        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            array2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            array2[ord(s2[r]) - ord('a')] += 1
            if array1 == array2:
                return True
        return False
