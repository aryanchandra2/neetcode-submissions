class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        removed = set(nums)
        return len(removed) != len(nums)

         