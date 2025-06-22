import math


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        while x != 0:
            digit = x % -10 if x < 0 else x % 10
            result += digit

            x = int(math.ceil(x / 10.0) if x < 0 else math.floor(x / 10.0))
            if x != 0:
                result *= 10

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31) + 1

        if result >= INT_MAX or result < INT_MIN:
            return 0

        return result
