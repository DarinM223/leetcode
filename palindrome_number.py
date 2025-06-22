class Solution:
    """
    Solution reverses the integer, then checks if the reversed integer
    equals the original integer. If it does, it's a palindrome
    """

    def reverseInteger(self, n: int) -> int:
        """
        Reverses a number and returns the reversed number
        """
        result = 0
        while n != 0:
            digit = n % 10
            result += digit
            n //= 10
            if n != 0:
                result *= 10

        return result

    def isPalindrome(self, x: int) -> bool:
        # for some reason negative numbers don't count
        if x < 0:
            return False
        return self.reverseInteger(abs(x)) == abs(x)
