'''
很简单,把它encode进去一个hashmap,然后根据字符的位置来decode就行
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def encode(string):
            str_hash = [ 0 for i in range(26)]
            for i in string:
                charidx = ord(i) - ord('a')
                str_hash[charidx] += 1
            # print(str_hash)
            for j in range(len(str_hash)):
                if str_hash[j] >= 10:
                    str_hash[j] = 'a' + str(str_hash[j]) + 'a'
                str_hash[j] = str(str_hash[j])
            # print(str_hash)
            return ''.join(str_hash)

        resmap = {}
        for i in strs:
            code = encode(i)
            # print(i, code)
            if code in resmap.keys():
                resmap[code].append(i)
            else:
                resmap[code] = [ i ]
        
        return list(resmap.values())
        