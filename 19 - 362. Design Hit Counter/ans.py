"""
python 实现ordered_map
直接使用min函数
"""

class HitCounter:

    def __init__(self):
        self.hitmap = {}
        

    def hit(self, timestamp: int) -> None:
        if timestamp in self.hitmap:
            self.hitmap[timestamp] += 1
        else:
            self.hitmap[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        if len(self.hitmap) > 0:
            mintime = min(self.hitmap)
        else:
            return 0
        while mintime <= timestamp - 300:
            self.hitmap.pop(mintime)
            if len(self.hitmap) > 0:
                mintime = min(self.hitmap)
            else:
                break
        res = 0
        for k,v in self.hitmap.items():
            res += v
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)