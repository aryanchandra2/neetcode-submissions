class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            curP = prices[r] - prices[l]
            maxP = max(curP, maxP)
            if prices[l] <= prices[r]:
                r += 1
            else:
                l += 1      
        return maxP