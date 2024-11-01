from typing import List
'''
有两种解法
第一种是记忆化递归,每一次递归记录字符的两段:
wordbreak('') and 'aaaa' in wordDict
wordbreak('a') and 'aaa' in wordDict
...
....
然后如果发现一个词已经解决了,把它存在字典里面:
resdict['a'] = False
resdict['aa'] = True
...
这样可以减少递归的复杂度

第二种是动态规划
dp[i] 代表字符串从0到i-1是否能被分解

对于i从0到n

然后再循环一次从0到i
那么dp[i] = dp[j] and s[j:i] in wordDict
这样通过两个循环就能找到dp的值
返回dp[n]

'''



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for faster lookups
        wordSet = set(wordDict)
        
        # dp[i] will be True if s[0:i] can be segmented using words from wordSet
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty substring can always be segmented

        # Iterate over each possible endpoint i for substrings s[0:i]
        for i in range(1, len(s) + 1):
            # Check each possible starting point j for the substring ending at i
            for j in range(i):
                # If s[0:j] can be segmented (dp[j] is True) and s[j:i] is in wordSet,
                # then s[0:i] can also be segmented
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # No need to check further if dp[i] is already True

        # The final result is whether the entire string s can be segmented
        return dp[len(s)]



# class Solution:

#     # def helper(self, sl, sr):
    
#     def helper(self, s, wordDict, resdict):

#         if s in resdict:
#             return resdict[s]
#         if len(s) == 0:
#             if not s in resdict:
#                 resdict[s] = True
#             return True

#         if s in wordDict:
#             if not s in resdict:
#                 resdict[s] = True
#             return True
        
#         for i in range(len(s)):
#             sl = s[0:i]
#             sr = s[i:]
#             if self.helper(sl,wordDict,resdict) and sr in wordDict:
#                 if not s in resdict:
#                     resdict[s] = True
#                 return True
#         if not s in resdict:
#                 resdict[s] = False
#         return False



#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         resdict = {}
#         return self.helper(s, wordDict, resdict)


        


        