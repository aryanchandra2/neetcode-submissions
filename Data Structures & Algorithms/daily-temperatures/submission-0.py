class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                tuple_ = stack.pop()
                ret[tuple_[1]] = i - tuple_[1]
            stack.append((temperatures[i], i))

            #38, 1  30, 2  3
            #
        return ret