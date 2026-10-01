class Solution:
    def asteroidCollision(self, asteroids):
        def repeater(asteroids):
            stack=[0]
            stack.append(asteroids[0])
            top=1
            for i in range(1,len(asteroids)):
                if asteroids[i]<0:
                    if stack[top]>0:
                        if abs(asteroids[i])>stack[top]:
                            stack.pop()
                            stack.append(asteroids[i])
                        elif abs(asteroids[i])==stack[top]:
                            stack.pop()
                            top-=1
                        else:
                            pass
                    else:
                        stack.append(asteroids[i])
                        top+=1
                else:
                    stack.append(asteroids[i])
                    top+=1
            return stack[1:]
        temp=asteroids
        temp2=repeater(temp)
        while temp!=temp2:
            if temp2==[]:
                return []
            temp=temp2
            temp2=repeater(temp)
        return temp
a=Solution()
print(a.asteroidCollision([1,-1,-2,-2]))