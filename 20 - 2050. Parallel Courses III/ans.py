import heapq


"""
still, use the priority queue with the key-value structure
"""


def heap_push(pq, pq_key, pq_value):
    heapq.heappush(pq, (pq_value, pq_key))

def heap_pop(pq, my_dict):
    while pq:
        v, k = heapq.heappop(pq)
        if my_dict[k] == v:
            return (k, v)
    return (-1, -1)

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        self.indegree_dict = {}
        self.next_edge = [ set() for i in range(n+1)]
        courses = [ i for i in range(1, n+1)]
        course_set = set(courses)
        finish_time = time
        finish_time = [0] + finish_time
        
        for i in relations:
            prev = i[0]
            nex = i[1]
            if nex in course_set:
                course_set.remove(nex)
            if nex in self.indegree_dict:
                self.indegree_dict[nex] += 1
            else:
                self.indegree_dict[nex] = 1
            
            self.next_edge[prev].add(nex)
        pq = []

        for k,v in self.indegree_dict.items():
            heap_push(pq,k,v)
        
        for i in course_set:
            heap_push(pq, i, 0)
            self.indegree_dict[i] = 0
       
        res = 0

        while len(pq) > 0:
            course, in_degree = heap_pop(pq,self.indegree_dict)
            '''
            use the priority queue to go through the course
            '''
            while in_degree == 0:
                next_edg = self.next_edge[course]
                t = time[course-1]
                res = max(finish_time[course], res)
                for j in next_edg:
                    self.indegree_dict[j] -= 1
                    heap_push(pq, j, self.indegree_dict[j])
                    '''
                    need to update the finish time array with the current course 
                    and the next course
                    '''
                    finish_time[j] = max(finish_time[j], finish_time[course] + time[j-1])
                course, in_degree = heap_pop(pq, self.indegree_dict)
        return res


        
            








        