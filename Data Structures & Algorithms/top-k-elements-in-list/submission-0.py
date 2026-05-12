class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        #counts is indexed by frequency of num
        counts = [[] for i in range(len(nums) + 1)]
        for num in freq.keys():
            counts[freq[num]].append(num)

        #i is each frequency
        i = len(counts) - 1
        while counts[i] == []:
            i-=1
        
        res = []
        for s in range(i, 0, -1):
            for j in counts[s]:
                if k > 0:
                   k-=1 
                   res.append(j)
    
        return res            
