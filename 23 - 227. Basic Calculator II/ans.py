class Solution:

    '''
    用数字栈和符号栈
    遇到数字入栈
    遇到符号,如果符号栈是空,入栈
    否则跟符号栈栈顶的符号比较
    如果符号栈栈顶的符号的优先级小于当前符号,直接入栈
    否则如果当前符号的优先级大于或者等于符号栈栈顶,
    需要先弹出符号栈栈顶元素,并弹出数字进行计算
    计算完之后,将数字入栈。
    重复直到优先级满足
    '''

    def isUpper(self, s, r):
        if (r == '*' or r == '/' or r == '+' or r == '-') and (s == '+' or s == '-'):
            return True
        if (r == '*' or r == '/' ) and (s == '*' or s == '/'):
            return True
        return False

    def operate(self, left, right, op):
        if op == '+':
            return left + right
        
        if op == '-':
            return left - right
        
        if op == '*':
            return left * right
        
        if op == '/':
            return left // right

    def calculate(self, s: str) -> int:


        num_stack = []
        mark_stack = []

        i = 0
        while i < len(s):
            
            char = s[i]
            # print(i, char)
            if char == ' ':
                i+=1
                continue
            if char.isdigit():
                t = i+1
                while t < len(s) and s[t].isdigit():
                    char += s[t]
                    t += 1
                    print(char, t)
                i = t-1
                num = int(char)
                num_stack.append(num)
            else:
                
                while len(mark_stack) > 0 and self.isUpper(char, mark_stack[-1]):
                    topmark = mark_stack.pop()
                    right = num_stack.pop()
                    left = num_stack.pop()
                    newnum = self.operate(left, right, topmark)
                    num_stack.append(newnum)
                mark_stack.append(char)
            
            i += 1
          
            
        if len(mark_stack) == 0:
            return num_stack[-1]
        else:
            while len(mark_stack) > 0:
                topmark = mark_stack.pop()
                right = num_stack.pop()
                left = num_stack.pop()
                newnum = self.operate(left, right, topmark)
                num_stack.append(newnum)
        return num_stack[-1]

                    
                
        