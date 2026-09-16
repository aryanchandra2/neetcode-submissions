class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i1 = 0
        self.i2 = 0
        self.turn = 1

    def next(self) -> int:
        if self.i1 < len(self.v1) and (self.turn == 1 or self.i2 >= len(self.v2)):
            item = self.v1[self.i1]
            self.i1 += 1
            self.turn = 2
            return item

        item = self.v2[self.i2]
        self.i2 += 1
        self.turn = 1
        return item

    def hasNext(self) -> bool:
        return self.i1 < len(self.v1) or self.i2 < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
