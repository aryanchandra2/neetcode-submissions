class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ret = 0
        for i in range(len(prices)-1):
            ret = max(ret, prices[r] - prices[l])
            
            if prices[r] < prices[l]:
                l = r
            r+=1
        return ret
         
