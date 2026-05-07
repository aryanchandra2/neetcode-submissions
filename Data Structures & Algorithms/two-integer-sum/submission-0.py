class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_map = {} 
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in i_map:
                return [i_map[complement], i]
            i_map[nums[i]] = i_map.get(nums[i], i)
        return []
        