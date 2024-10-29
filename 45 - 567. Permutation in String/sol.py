'''
用字典计数，然后用滑动窗口计算结果
'''


class Solution:


        
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        temp = s1
        s1 = s2
        s2 = temp

        s2hash = {}

        for i in s2:
            if not i in s2hash:
                s2hash[i] = 0
            s2hash[i] += 1
        
        l = 0
        r = len(s2) -1

        s1hash = {}
        
        for i in range(l,r+1):
            if not s1[i] in s1hash:
                s1hash[s1[i]] = 0
            s1hash[s1[i]] += 1

        # print('first', s1hash)
        res = False
        if self.hashequ(s1hash, s2hash):
            return True
        
        # r += 1
        r += 1
        for i in range(r, len(s1)):
            # substr = s1[l:r+1]
            if s1[r] in s1hash:
                s1hash[s1[r]] += 1
                
            else:
                s1hash[s1[r]] = 1
            
            # print(l, r, s1hash, s1[l], s1[r])
            s1hash[s1[l]] -= 1
            if s1hash[s1[l]] == 0:
                del s1hash[s1[l]]
            l += 1
            if s1hash == s2hash:
                return True
            r += 1
        return res
             


            

            

        