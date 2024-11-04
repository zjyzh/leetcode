"""
两个函数,一个遍历从当前pos开始的回文数列,
一个遍历从当前gap开始的回文数列

可以简化成一个函数

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome (single center)
            odd_palindrome = expand_around_center(i, i)
            # Even-length palindrome (pair center)
            even_palindrome = expand_around_center(i, i + 1)
            # Update the longest palindrome found
            longest = max(longest, odd_palindrome, even_palindrome, key=len)
        
        return longest




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
            
        