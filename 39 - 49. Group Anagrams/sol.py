from collections import defaultdict
from typing import List

'''
高阶的质数hash方法，通过构建质数hash来构建结果，提升时空复杂度
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Map each character to a unique prime number
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
                  59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        def get_prime_product(s: str) -> int:
            # Calculate the product of primes based on character frequency
            product = 1
            for char in s:
                product *= primes[ord(char) - ord('a')]
            return product

        # Use defaultdict to collect anagrams
        anagrams = defaultdict(list)
        
        for s in strs:
            # Calculate unique product for each string
            key = get_prime_product(s)
            anagrams[key].append(s)

        # Return the grouped anagrams
        return list(anagrams.values())


'''
简单直观的方法，用字符串来进行encode
通过频率来构建一个字符数组，然后返回
'''


# class Solution:

#     def encode(self, s, hashset):
        
#         for i in s:
#             hashset[ord(i) - ord('a')] += 1

#         res = '_'.join(map(str, hashset))
#         for i in range(26):
#             hashset[i] = 0
#         return res


#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         reshash = {}
#         hashset = [0 for i in range(26)]
#         for i in strs:
#             encodeed = self.encode(i,hashset)
#             if not encodeed in reshash:
#                 reshash[encodeed] = []
#             # print(i, encodeed)
#             reshash[encodeed].append(i)
#         return list(reshash.values())
        



        