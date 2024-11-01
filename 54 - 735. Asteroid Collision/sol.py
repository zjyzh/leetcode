from typing import List
'''

stack 经典题目,用stack就行了


'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            # Handle potential collisions
            while stack and asteroid < 0 < stack[-1]:
                # Both asteroids have the same size, both explode
                if stack[-1] == -asteroid:
                    stack.pop()
                    break
                # Top of the stack asteroid is smaller, it explodes
                elif stack[-1] < -asteroid:
                    stack.pop()
                    continue
                # New asteroid is smaller, it explodes
                else:
                    break
            else:
                # No collision, add asteroid to stack
                stack.append(asteroid)
        
        return stack



# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:

#         res = []
#         cur = asteroids.pop()
#         res.append(cur)
        
#         while len(asteroids) > 0:

#             if len(res) == 0:
#                 nx = asteroids.pop()
#                 res.append(nx)
#                 continue

#             nxt = asteroids[-1]
#             current = res[-1]

#             if current < 0 and nxt > 0:

#                 if abs(current) > abs(nxt):
#                     asteroids.pop()
#                 elif abs(current) == abs(nxt):
#                     res.pop()
#                     asteroids.pop()  
#                 else:
#                     res.pop()
#                 continue
                
#             res.append(nxt)
#             asteroids.pop()

#         res.reverse()
#         return res

#             # if current > 0 and nxt > 0

            

        
        