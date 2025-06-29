class Solution(object):
    """
    Solution: For every character in the string, first
    go through all duplicates after it
    until you can find a range from start-end.

    Then move the start counter back and the end counter
    forward and check if they are the same number and repeat
    while recording the length until either the start is not
    equal to the end or either of them go outside the array.

    Then save the max length and the max range from the start
    and end. Then at the end, return the saved max substring.

    Time Complexity: O(N^2) (not the most efficient but reasonable)
    """

    def longestPalindrome(self, s: str) -> str | None:
        # for every character attempt to move outward

        maxLength = 0
        maxSubstr = None

        if len(s) == 1:
            return s[0]

        for i in range(0, len(s)):
            length = 1
            start, end = i, i

            # go through duplicate characters to find the end
            for j in range(i + 1, len(s)):
                if s[j] == s[i]:
                    length += 1
                    end = j
                else:
                    break

            startStr, endStr = start, end

            # move pointers outward to see if they are equal
            while start >= 0 and end < len(s) and s[start] == s[end]:
                length += 2
                startStr, endStr = start, end
                start -= 1
                end += 1

            if length > maxLength:
                maxLength = length
                maxSubstr = (startStr, endStr)

        if maxSubstr == None:
            return None
        else:
            return s[maxSubstr[0] : maxSubstr[1] + 1]
