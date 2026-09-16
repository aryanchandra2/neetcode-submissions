import random
class Solution:

    def __init__(self, w: List[int]):
        self.rangeSums = [w[0]]
        for i in range(1, len(w)):
            self.rangeSums.append(w[i] + self.rangeSums[-1])


    def pickIndex(self) -> int:
        l, r = 0, len(self.rangeSums) - 1
        pick = random.randint(1, self.rangeSums[r])
        while l < r:
            m = (l + r) >> 1
            
            if pick > self.rangeSums[m]:
                l = m + 1
            elif pick < self.rangeSums[m]:
                r = m
            else:
                return m

        return l
