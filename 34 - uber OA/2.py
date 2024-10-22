"""

给一个list query, 和一个int diff。query中有两种元素
“+x” 往当前nums中添加一个int x
“-x“ 去掉nums中所有数字 x
定义 一个triple (x,y,z), y-x=z-y=diff
输出每个query过后nums中元素可以组成的triple个数，相同的数字可以多次使用（比如nums=[1,2,3,1] diff=1 输出就是2）
query = ['+1', '+2', '+3', '+1', '-1'] diff=1
output=[ 0, 0, 1, 2, 0]


"""

print(f'*{word.center(width)}*')
