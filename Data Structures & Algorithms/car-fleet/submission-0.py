class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        pairs = sorted(pairs)
        stack = []
        for p,s in reversed(pairs):
            if not stack or (target - p)/s > stack[-1]:
                stack.append((target - p)/s)
            
        return len(stack)
            

            

        