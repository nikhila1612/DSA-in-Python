class Solution:
    def isVAlid(self,s):
        stack=[]
        brackets={")":"(","}":"{","]":"["}
        for i in s:
            if i in brackets.values():
                stack.append(i)
            else:
                if not stack or brackets[i]!=stack.pop():
                    return False
        return not stack
    
solution1 = Solution()
print(solution1.isVAlid('({[]})'))