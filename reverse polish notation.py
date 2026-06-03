class Solution:
    def evalRPN(self, tokens):
        stack=[];expres=['+', '-', '*','/']
        for i in tokens:
            if i not in expres:
                stack.append(int(i))
            else:
                a=stack.pop()
                b=stack.pop()
                if i=='+':
                    stack.append(a+b)
                elif i=='*':
                    stack.append(a*b)
                elif i=='/':
                    if b//a>0:
                        stack.append(b//a)
                    else:
                        stack.append(-(-b//a))
                else:
                    stack.append(b-a)
        return stack[0]
a=Solution()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(a.evalRPN(tokens))