M = 1000000007

class Solution(object):


    def findNext(self, target):
        self.next = [ 0 for i in range(len(target) )]
        i = 0
        j = -1
        self.next[i] = j

        while i < len(target) -1:
            if j == -1 or target[i] == target[j]:
                i += 1
                j += 1
                self.next[i] = j
            else:
                j = self.next[j]
    
    def countSubStr(self, original, target):

        i = 0
        j = 0
        self.findNext(target)

        res = 0
        while(i < len(original) ):

            if j >= len(target):
                res += 1
                i = i - j + 1
                j = 0

            if j == -1 or original[i] == target[j]:
                i += 1
                j += 1
            else:
                j = self.next[j]

        if j >= len(target):
            res += 1
        return res

    def quickMul(self, mat, N):
        if N == 0:
            return [1, 0 , 0 , 1]
        
        mat2 = self.quickMul(mat, N//2)
        # print('mat2', mat2)
        if N % 2 == 0:
            return self.multiply(mat2, mat2)
        else:
            return self.multiply(self.multiply(mat2, mat2), mat)



    def multiply(self, mat1, mat2):
        '''

        a1 b1         a2   b2
        c1 d1         c2   d2
        

        '''

        a1 = mat1[0]
        b1 = mat1[1]
        c1 = mat1[2]
        d1 = mat1[3]

        a2 = mat2[0]
        b2 = mat2[1]
        c2 = mat2[2]
        d2 = mat2[3]

        return [ (a1 * a2 + b1 * c2)%M, (a1 * b2 + b1 * d2)%M, 
                    (c1* a2 + d1 * c2)%M, (c1 * b2 + d1 * d2)%M ]
                    



    def numberOfWays(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: int
        """

        ss = s + s
        ss = ss[:len(ss) -1]
        # print(ss, t)
        """
        first step:  count the substr in double ss, 
        to see that the posibile option to transform
        from a non-target to target.
        p is the number of transforming the string into the target
        """
        p = self.countSubStr(ss, t)
        # print(p )

        n = len(s) 
        """
        in here, we have the transform matrix:

        {
            n - p - 1,    n - p
            p,            p -1
        }
        represent that we need to use it to do the step
        the original transformation looks like this:
        f[j] = (n - p - 1) * f[j-1] + (n-p) * g[j-1]
        g[j] = p*f[j-1] + (p-1)*g[j-1]

        in here, f[j] represent the bad number that we have after j times of transform
        g[j] represent the good number we have after j transform

        第一行的解释:对于j-1轮不匹配的字串,下一轮有n-p-1种操作依然得到不匹配的字串(因为不能shift成自己)。对于j-1轮已经匹配的字串,下一轮有n-p种操作变成不匹配的字串。同理第二行的解释:对于j-1轮不匹配的字串,下一轮有p种操作变成匹配的字串。对于j-1轮已经匹配的字串,下一轮有p-1种操作依然变成匹配的字串(因为不能shift成自己)。

        转移状态矩阵:
        {
            n - p - 1,    n - p
            p,            p -1
        }
        代表需要进行k次转移,因此需要矩阵的k次方
        [
            f[k],          =   [n - p - 1,    n - p          [f[0]
            g[k]                p,           p -1 ] ^ k   *   g[0]]
        ]

        """
        T = [ n -p - 1, n - p, p, p -1 ]
        # print(T)
        Tk = self.quickMul(T, k)
        # print(Tk)

        if s == t:
            return Tk[3] # { 0, 1 }'
        else:
            return Tk[2] # { 1, 0 }'



        # return 1

        
        