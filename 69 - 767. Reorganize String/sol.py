import heapq
from collections import Counter

'''
构建优先队列，按照字符出现的频率排序
每次从优先队列里面取出两个字符，然后把两个字符拼接在一起
随后把字符出现的频率减一，然后重新放入优先队列
重复，直到最后。

'''



class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequency of each character
        char_count = Counter(s)
        max_freq = max(char_count.values())
        if max_freq > (len(s) + 1) // 2:
            return ""  # Not possible to reorganize if max frequency is too high
        
        # Max heap for characters based on frequency
        max_heap = [(-freq, char) for char, freq in char_count.items()]
        heapq.heapify(max_heap)
        
        result = []
        while len(max_heap) > 1:
            # Pop two most frequent characters
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)
            # Append to result
            result.extend([char1, char2])
            
            # Decrease frequency and push back if still remaining
            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))

        # If one character remains, append it
        if max_heap:
            result.append(max_heap[0][1])

        return ''.join(result)



# import heapq

# class Solution:
#     def reorganizeString(self, s: str) -> str:

#         char_hash = {}
#         for i in s:
#             if i not in char_hash:
#                 char_hash[i] = 0
#             char_hash[i] += 1
#         pq = []
#         for i in char_hash.keys():
#             heapq.heappush(pq, [-char_hash[i], i])
#         if ( (-pq[0][0]) -1) > (len(s) - (-pq[0][0])):
#             return ''
        
#         res = ''
#         cur1 = None
#         # print(char_hash)
        
#         while len(res) < len(s) and len(pq) > 0:

#             # print(pq)
#             cur1 = heapq.heappop(pq)
#             cur1[0] = - cur1[0]

#             if len(pq) > 0:
#                 cur2 = heapq.heappop(pq)
#                 cur2[0] = - cur2[0]

#                 res += cur1[1]
#                 res += cur2[1]
#                 cur1[0] -= 1
#                 cur2[0] -= 1

#                 if cur1[0] > 0:
#                     cur1[0] = - cur1[0]
#                     heapq.heappush(pq, cur1)
                
#                 if cur2[0] > 0:
#                     cur2[0] = - cur2[0]
#                     heapq.heappush(pq, cur2)
#             else:
#                 res += cur1[1]
#                 break
            

            

#             # if cur2[0] > cur1[0]:
#             #     mid = cur2
#             #     cur2 = cur1
#             #     cur1 = mid
#             # print(cur1, cur2)
            
#             # while cur1[0] > 0 and cur2[0] > 0:
#             #     res += cur1[1]
#             #     res += cur2[1]
#             #     cur2[0] -= 1
#             #     cur1[0] -= 1
            
#             # if cur1[0] == 0:
#             #     if len(pq) > 0:
#             #         cur1 = heapq.heappop(pq)
#             #         cur1[0] = - cur1[0]
        
#         # if cur1[0] > 0:
#         #     res += cur1[1]
#         return res



            

        