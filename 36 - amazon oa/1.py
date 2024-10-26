
class Solution:
  def getMaxPrograms(self, time, m, k):
    res = 0
    curaccu = 0
    remain = k
    lessidx = m
    # idx = 0
    
    for j in range(len(time) - m):
      curres = 0
      remain = k
      lessidx = m
      idx = j
      while idx < len(time):
        i = time[idx]
        if lessidx == 0:
          break
        if i <= remain:
          curres += 1
          remain -= i
          idx += 1
        else:
          lessidx -= 1
          remain = k
      res = max(res, curres)
    return res
        

sol = Solution()
time = [5, 2, 1, 4, 2]
m = 2
k = 6
print("first, ", sol.getMaxPrograms(time, m, k))


time = [4, 2, 3, 4, 1]
m = 1
k = 4
print("second, ", sol.getMaxPrograms(time, m, k))

time = [1, 2, 3, 1, 1]
m = 3
k = 3
print("third, ", sol.getMaxPrograms(time, m, k))
