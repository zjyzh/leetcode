import math

class Solution(object):

    def solveOne(self, count, upgrade, sell, money):
        

        # remember the keypoint of bin search
        # is to define the upper and lower bound
        # every time get the mid
        # then change the upper and lower bound 
        # until it reached the correct solution
        low = 0
        high = count
        ans = 0
        while (low <= high):
            mid = low + (high - low) // 2
            totalCost = mid * upgrade
            totalMoney = money + (count - mid) * sell
            if totalMoney >= totalCost:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

        
    def maxUpgrades(self, count, upgrade, sell, money):
        """
        :type count: List[int]
        :type upgrade: List[int]
        :type sell: List[int]
        :type money: List[int]
        :rtype: List[int]
        """
        res  = []
        for i,j,k,w in zip(count, upgrade, sell, money):
            res.append(self.solveOne(i,j,k,w))
        return res





        