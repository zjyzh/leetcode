'''
use a map to store the char and it's idx
update the map accordingly
move l and r to match the string
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        if len(s) <= 1:
            return len(s)
        
        tempmap = {}

        tempmap[s[l]] = 0
        res = 0
        while r < len(s):

            cur_char = s[r]
            if cur_char in tempmap.keys():
                cur_len = r - l
                res = max(res, cur_len)
                next_l = tempmap[cur_char] + 1
                for i in range(l, next_l ):
                    del tempmap[s[i]]
                
                tempmap[s[r]] = r
                l = next_l
                r += 1
                
            else:
                tempmap[cur_char] = r
                r += 1
        
        res = max(res, r-l)

        return res





        