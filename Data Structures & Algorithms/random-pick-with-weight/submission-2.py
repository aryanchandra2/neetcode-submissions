import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = [w[0]]
        for i in range(1, len(w)):
            self.prefixSum.append(w[i] + self.prefixSum[-1])

    def pickIndex(self) -> int:
        l, r = 0, len(self.prefixSum) - 1
        pick = random.randint(0, self.prefixSum[-1])
        while l < r:
            m = (l + r) >> 1

            if pick < self.prefixSum[m]:
                r = m
            elif pick > self.prefixSum[m]:
                l = m + 1
            else:
                return m
        return r



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()