'''
这道题的题解跟之前的139类似,依然是递归求解+记忆化搜索

在我们递归的时候,依然还是从左到右:

wordbreak('') and 'aaaaa' in worddict
wordbreak('a') and 'aaaa' in worddict
wordbreak('aa') and 'aaa' in worddict
.....

但是当我们找到左边的wordbreak的时候,假设:
wordbreak('catsand') and 'dog' in worddict 
这个条件成立,那么这个时候,
reshash['catsand'] = { 'cats and', 'cat sand'}
然后我们需要遍历reshash['catsand']并将结果添加到reshash:
reshash = ["cats and dog","cat sand dog"]

同样的,要求wordbreak('catsand')
分成:
wordbreak('cat') and 'sand' in worddict 
wordbreak('cats') and 'and' in worddict 
这两个,这两个都会返回true
那么这个时候存储的为:
reshash['cat'] = ['cat']
reshash['cats'] = ['cats']
然后把他们都加入到
reshash['catsand'] = { 'cats and', 'cat sand'}
这样就能递归求解。

'''



class Solution:

    def helper(self, s, wordDict, reshash):

        if s in reshash:
            return True

        if len(s) == 0:
            if not s in reshash:
                reshash[s] = ['']
            return True

        curList = []

        canbreak = False
        for i in range(len(s)):
            
            sl = s[0:i]
            sr = s[i:]
            if self.helper(sl, wordDict, reshash) and sr in wordDict:
                for j in range(len(reshash[sl])):
                    strj = reshash[sl][j]
                    if not len(strj) == 0:
                        strj += " "
                    strj += sr
                    curList.append(strj)
                reshash[s] = curList
                canbreak = True
        
        return canbreak

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        reshash = {}

        self.helper(s, wordDict, reshash)

        if s in reshash:
            return reshash[s]
        else:
            return []




        