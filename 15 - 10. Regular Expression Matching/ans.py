"""

dp[i][j] -> if s[from 0 to i] and p[from 0 to j] is a match
dp[0][0] = true

initially, we need to do a pre step to process this condition:

p = "a*"
s =  ""

dp[0][0] = true

for j in range(len(p)):
    if p[j] == "*" and dp[0][j-2] == True:
        dp[0][j] = True

this step is to judge the case that initially the condition is null



1. p[j] == s[i]  : dp[i][j] = dp[i-1][j-1]
2. if p[j] == '.' dp[i][j] = dp[i-1][j-1]
3. if p[j] == '*':
    two different condition
        1. if p[j-1] != s[i] : dp[i][j] = dp[i][j-2]
        2. if p[j-1] == s[i] or p[j-1] == '.'
            dp[i][j] = dp[i][j-1]  -> a* count as single a
            dp[i][j] = dp[i-1][j]  -> a* count as multiple a 
            dp[i][j] = dp[i][j-2]  -> a* count as empty

            
since dp[i][j] start from 1 and p[i] s[i] start from 0
every i, j related to dp[i][j] should become i+1, j+1


"""





class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [ [False for i in range(len(p) + 1)] for j in range(len(s) + 1) ]
        dp[0][0] = True
        
        for j in range(1, len(p)):
            if p[j] == '*' and dp[0][j-1]:
                dp[0][j+1] = True


        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i]: 
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    elif p[j-1] == s[i] or p[j-1] == '.':
                        dp[i+1][j+1] = (dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]) 
        i = len(s)
        j = len(p)
        return dp[i][j]
        