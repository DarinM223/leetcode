from typing import Literal


class Solution:
    def isValid(self, s: str) -> bool:
        opStack: list[Literal["(", "{", "["]] = []

        matchMap = {"(": ")", "{": "}", "[": "]"}

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                opStack.append(ch)
            elif ch == ")" or ch == "}" or ch == "]":
                if len(opStack) > 0:
                    if matchMap[opStack[-1]] == ch:
                        opStack.pop()
                    else:
                        return False
                else:
                    return False
        return len(opStack) == 0
