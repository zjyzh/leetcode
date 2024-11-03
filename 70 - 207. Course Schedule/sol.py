
from collections import deque, defaultdict
from typing import List

'''
拓扑排序，把出度为0的节点放在队列，然后把指向它的边都消除
注意我们不需要用优先队列，只需要用普通队列
可以用一个数记录已经完成的课程数量，以此返回结果

'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list and in-degree count for each course
        course_map = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prerequisite in prerequisites:
            course_map[prerequisite].append(course)
            in_degree[course] += 1
        
        # Step 2: Initialize queue with courses having zero in-degree (no prerequisites)
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])

        # Step 3: Process courses in topological order
        completed_courses = 0
        while queue:
            course = queue.popleft()
            completed_courses += 1

            for next_course in course_map[course]:
                in_degree[next_course] -= 1  # Reduce in-degree by 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)  # Add next course if it has no remaining prerequisites

        # Step 4: Check if all courses were completed
        return completed_courses == numCourses



# import heapq

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         coursemap = {}
#         outdegree = [0 for i in range(numCourses)]

#         for i in prerequisites:
#             after = i[0]
#             before = i[1]
#             if before not in coursemap:
#                 coursemap[before] = []
#             coursemap[before].append(after)
#             outdegree[after] += 1
            
        
#         pq = []
#         for i in range(numCourses):
#             if outdegree[i] == 0:
#                 heapq.heappush(pq,[outdegree[i],i])
        
#         finishset = set()
#         if len(pq) ==0:
#             return False
#         while len(pq) > 0:
#             top = heapq.heappop(pq)
#             if top[0] > 0:
#                 return False
#             else:
#                 if top[1] in coursemap:
#                     for j in coursemap[top[1]]:
#                         outdegree[j] -= 1
#                         if outdegree[j] ==0:
#                             heapq.heappush(pq, [0, j])
#                 finishset.add(top[1])
#         if len(finishset) == numCourses:
#             return True
#         else:
#             return False

            
        

        


        