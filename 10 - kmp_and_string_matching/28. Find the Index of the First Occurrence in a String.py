class Solution(object):


    # KMP algorithm - this is correct one 
    # remember to add -1 in the front
    # to use it, just use the simple judgement:
    '''
    
    if j == -1 or haystack[i] == needle[j]:
        i += 1
        j += 1
    else:
        j = self.next[j]
    
    '''


    def computeNext(self, target):
        self.next = [0 for i in range(len(target) + 1)]

        i  = 0
        j = -1
        self.next[i] = j
        while i < len(target) - 1:
            # print( i, j)
            if j == -1 or target[i] == target[j]:
                i += 1
                j += 1
                self.next[i] = j
            else:
                j = self.next[j]
                
            

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        i = 0
        j = 0

        self.computeNext(needle)
        
        
        # needle = "#" + needle
        # haystack = "#" + haystack

        i = 0
        j = 0

        # print(self.next)
        # if haystack == needle:
        #     return 0
        while i < len(haystack):
            """
            neet to remember this : if you don't want to terminate it,
            just record the number and skip it 
        
            """
            if j >= len(needle):
                if i - j >=0:
                    return i - j
                else:
                    return 0
            
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = self.next[j]
            
        if j >= len(needle):
            if i - j >=0:
                return i - j
            else:
                return 0
                
        return -1


        