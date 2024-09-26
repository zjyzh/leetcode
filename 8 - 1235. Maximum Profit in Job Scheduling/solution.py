class Solution(object):

    def find_target(self, order_list, target):
        # find the first key that less than target
        low = 0
        up = len(order_list) - 1 
        mid = (up - low) // 2
        res = 0

        # if len(order_list) == 0:
        #     return None
        # if len(order_list) > 0 and order_list[0][0] > target:
        #     return None

        while low <= up:
            # print("mid ", mid, "low ", low, 'up ', up)
            if order_list[mid][0] <= target:
                 res = mid
                 low = mid +1
            else:
                up = mid - 1
            
            mid = low + (up - low) // 2
        return res


    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """

        '''
        dp[i] = maxProfit I can get from 1 to i
        dp[i] = max (val[i] , dp[j] + val[i])
        '''

        missions = []
        for i in range(len(endTime)):
            start = startTime[i]
            end = endTime[i]
            pro = profit[i]
            missions.append((start,end,pro))
        # step 1 : we need to sort the list using the end time
        missions = sorted(missions, key=lambda x: x[1])

        # step 2 : add a dummy dp point
        dp = []
        dp.append((-1, 0))
        # dp is to store the history value of the max
        # key - value
        # key is end
        # val is maxvalue that smaller than end
        # since our loop will start from the smaller end, so
        # this dp array is ordered by the key
        # we can use binary search to serch the cloest key

        formal_max_value = 0
        for i in range(len(missions)):
            mis = missions[i]
            start = mis[0]
            end = mis[1] 
            val = mis[2]

            # step 3: find the cloest target that smaller and start
            
            formal_max_value = self.find_target(dp, start)

            # step 4: find the cloest target that smaller than end
            max_value_index_in_interval = self.find_target(dp, end)
            
            res = 0
            max_value_in_inter = 0
            if max_value_index_in_interval > formal_max_value:
                max_value_in_inter = dp[max_value_index_in_interval][1]

            
            """
           
            max value between choose the current interval or not choose the 
            current interval
            dp[formal_max_value][1] + val we choose to use the value of interval
            which means that we pickup a value that compabial with the 
            starttime

            """



            """
            max_value_in_inter means that we don't choose the inter
            then find max value that not compatible with it
            """
            res = max(dp[formal_max_value][1] + val, max_value_in_inter)
            dp.append((end, res)) 
           
        return dp[-1][1]

       
        
   