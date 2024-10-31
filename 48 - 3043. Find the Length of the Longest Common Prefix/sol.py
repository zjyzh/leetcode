'''
比较优雅的通用前缀树的实现
tire tree

'''



class Tire:
    def __init__(self):
        self.tire = {}

    def add_word(self,word):
        tire = self.tire
        for c in word:
            tire = tire.setdefault(c, {})
        tire['eos'] = word
        return
    
    def find_prefix(self, word):
        tire = self.tire
        depth = 0
        for c in word:
            if c in tire:
                tire = tire[c]
                depth += 1
            else:
                break
        return depth


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        tire = Tire()
        for i in arr1:
            tire.add_word(str(i))
        res = 0
        for j in arr2:
            temp = tire.find_prefix(str(j))
            res = max(temp, res)
        return res