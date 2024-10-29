"""
两个函数，一个遍历从当前pos开始的回文数列，
一个遍历从当前gap开始的回文数列
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def getPalid(s, pos):
            l = pos - 1
            r = pos + 1

            if l < 0 or r >= len(s) or s[l] != s[r]:
                return (-1, -1)

            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            
            return (l + 1, r -1)
        
        def getGap(s, l, r):
            if l < 0 or r >= len(s) or s[l] != s[r]:
                return (-1, -1)
            
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            return (l + 1, r -1)

        dis = 0
        resr = 0
        resl = 0
        for i in range(len(s)):
            l ,r = getPalid(s, i)
            if l != -1:
                if (r - l + 1) > dis:
                    dis = (r - l + 1)
                    resr = r
                    resl = l
            
            l, r = getGap(s, i, i +1)

            if l != -1:
                if (r - l + 1) > dis:
                    dis = (r - l + 1)
                    resr = r
                    resl = l

        
        return s[resl:resr + 1]
            
        