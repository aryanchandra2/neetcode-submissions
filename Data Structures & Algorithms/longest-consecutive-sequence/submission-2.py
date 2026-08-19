class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numset = set(nums)
        res = 1
        cur = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                cur = 1
                while nums[i] + cur in numset:
                    cur += 1
                    res = max(cur, res)

        return res
            

            
