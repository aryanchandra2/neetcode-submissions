class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curA = min(heights[l], heights[r]) * (r-l)
            if curA > maxA:
                maxA = curA

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return maxA



        # we move the lesser one to optimize, and since we go through all widths then it is good
            


        