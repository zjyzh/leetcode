from collections import defaultdict
import copy
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        self.dist = defaultdict(int)
        for i in p:
            self.dist[i] += 1
        # print(self.dist)
        res = []
        slide_window = defaultdict(int)
        for j in s[:len(p)]:
            slide_window[j] += 1

        # if self.dist == slide_window:
        #     res.append(0)
        for i in range(len(p), len(s) +1):
            
            if self.dist == slide_window:
                res.append(i - len(p))
            
            # print( i , i - len(p))
            # print(self.dist , slide_window)
            if i == len(s):
                break
            
            end = s[i]
            ini = s[i - len(p)]
            slide_window[ini] -= 1
            slide_window[end] += 1
            if(slide_window[ini] == 0):
                del slide_window[ini]
            


            # # print(substr)
            # if self.isAnagram(substr):
            #     res.append(i)
        return res

    def isAnagram(self, s1):
        tempdict = copy.copy(self.dist)
        for i in s1:
            if tempdict[i] == 0:
                return False
            else:
                tempdict[i] -= 1
        
        return True

            
        