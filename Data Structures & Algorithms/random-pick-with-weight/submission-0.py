import random
class Solution:

    def __init__(self, w: List[int]):
        self.newList = []
        for i, weight in enumerate(w):
            self.newList.extend([i] * weight)


    def pickIndex(self) -> int:
        return self.newList[random.randint(0, len(self.newList) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()