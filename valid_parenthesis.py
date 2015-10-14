class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opStack = []
        
        matchMap = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                opStack.append(ch)
            elif ch == ')' or ch == '}' or ch == ']':
                if len(opStack) > 0:
                    if matchMap[opStack[-1]] == ch:
                        opStack.pop()
                    else:
                        return False
                else: 
                    return False
        return len(opStack) == 0
