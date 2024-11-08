from collections import defaultdict

    # dp[i][k] : in the ith target and kth char_words, how many ways for us to use
    # dp[i][k] = dp[i][k-1] (we don't use the kth char)
    # dp[i][k] += dp[i-1][k-1] * count( how many char we found in the kth char_words) we use kth char
    # return dp[n][m] 
    # n = len(target)
    # m = len(word)



class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        char_words = [ defaultdict(int) for i in range(len(words[0]) + 1)]
        for i in words:
            for j in range(1,len(i)+1):
                # char_words[j] = defaultdict(int)
                char_words[j][i[j-1]] += 1
        
        
        n = len(target)
        m = len(words[0])
        dp = [ [0 for i in range(m+1)] for j in range(n+1) ]

        # char_words[i] -> the distribution of char in ith target
        
        target = '#' + target # you need to have the 0 prosition
       
        for i in range(m+1):
            dp[0][i] = 1 # the 0th should be 1

        for i in range(1, n+1):
            for k in range(1, m+1 ):
                dp[i][k] = dp[i][k-1] # you should do this whenever the roop
                if char_words[k][target[i]] > 0:
                    dp[i][k] += (dp[i - 1][k-1] * char_words[k][target[i]]) % 1000000007
                    dp[i][k] = dp[i][k] % (1000000007)
                    

        return dp[n][m]





        