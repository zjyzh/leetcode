'''
用栈来进行行为模拟
注意就是栈的顺序跟原来的字符的顺序不一样
要reverse一下

'''



class Solution:

    def getNum(self, s, i):
        num = s[i]
        idx = i + 1
        for j in range(2):
            if s[idx].isdigit():
                num += s[idx]
                idx += 1
        return (int(num), idx)
    
    

    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            char = s[i]
            # print(stack, char)

            if char.isdigit():
                (num, nextidx) = self.getNum(s,i)
                i = nextidx
                stack.append(num)
                continue
            
            if char == '[':
                stack.append(char)
                i += 1
                continue
            
            if char == ']':
                countchar = []
                while stack and stack[-1] != '[': 
                    c = stack.pop()
                    countchar.append(c)
                stack.pop()
                num = stack.pop()
                
                countchar.reverse()
                tchar = ''.join(countchar)
                newstr = num*tchar
                stack.append(newstr)
                i += 1
                continue
            
            stack.append(char)
            i += 1
        return ''.join(stack)
            
            
                


        



        