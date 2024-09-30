from collections import defaultdict
import heapq

"""
this is a method to impliment the min-heap
insert the key-value to the min-heap
then pop the new updated value from the heap
"""

def update_dict_and_heap(mydict, heap, key, new_value):
    mydict[key] = new_value
    heapq.heappush(heap, (new_value, key))

def get_min_from_heap(heap, mydict):
    while heap:
        """
        in here, we need to do a loop to pop the heap.
        if the heap is not equal to our dict
        then we need to discard it and do another loop
        """
        v, k = heapq.heappop(heap)
        if mydict[k] == v:
            return (k, v)
    
    return (-1, -1)



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        """
        this is a dict to store the in-degree
        """
        in_degree_dict = [ 0 for i in range(numCourses) ]

        """
        this is a set to store the out-edge
        """
        out_edge = [ set() for i in range(numCourses)]

        """
        ini the in_degree_dict and out_edge
        """
        for i in prerequisites:
            outnode = i[1]
            in_n = i[0]
            in_degree_dict[in_n] += 1
            out_edge[outnode].add(in_n)
        
        pq = []
        
        """
        need to do a loop to ini the priority queue
        """
        for i in range(numCourses):
            indegree = in_degree_dict[i]
            update_dict_and_heap(in_degree_dict, pq, i, indegree)
        
        
        res = []
        while(len(pq) > 0):
            """
            get the node and degree from the priority queue
            """
            (node, degree) = get_min_from_heap( pq, in_degree_dict)
            if(degree == -1):
                # this means that the pq is empty
                break
            
            # the min in_degree is 0, do a loop to append res and 
            # delete all of the out edge from this node
            if degree == 0:
                res.append(node)
                out = out_edge[node]
                for j in out:
                    in_degree_dict[j] -= 1
                    update_dict_and_heap(in_degree_dict, pq, j, in_degree_dict[j])
                out_edge[node] = set()
            else:
                # if it's not 0, return the empty, since it's posible that
                # it will turn to the loop
                return []

        return res