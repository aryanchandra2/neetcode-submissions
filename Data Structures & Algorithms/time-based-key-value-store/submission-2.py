class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value, timestamp))
        else:
            self.timemap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        largestTime = float("-inf")
        largestVal = ""
        
        if key in self.timemap:
            values = self.timemap[key]
            l, r = 0, len(values) - 1
            while l <= r:
                m = (l + r) // 2

                if values[m][1] <= timestamp:
                    l = m + 1
                    largestVal = values[m][0]
                elif values[m][1] > timestamp:
                    r = m - 1
            
        return largestVal




            # for v, t in self.timemap[key]:
            #     if t <= timestamp:
            #         if t > largestTime:
            #             largestTime = t
            #             largestVal = v
        return largestVal
        
        
                
