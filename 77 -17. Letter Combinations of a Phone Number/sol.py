
'''
简单直观的暴力方法
把所有的数字都放在数组里面，然后每一次都乘一次数组
'''


class Solution:

    def addnew(self, res_set, new_set):
        
        new_res = []
        for i in res_set:
            for j in new_set:
                tres = i+j
                new_res.append(tres)
        return new_res


    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits)== 0:
            return []
        digitmap = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        digit_list = list(digits)

        ini = list(digitmap[digit_list[0]])
        resset = ini
        for i in range(1,len(digit_list)):
            new_nums = list(digitmap[digit_list[i]])
            resset = self.addnew(resset,new_nums)
        return resset


        