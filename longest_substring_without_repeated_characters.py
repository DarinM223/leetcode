class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        letterSet = set[str]()
        start, end = 0, 0
        repeatedChar = None
        curr_len, max_len = 0, 0

        while start <= end and end < len(s):
            if repeatedChar != None:
                # move up start position removing characters from set
                letterSet.remove(s[start])
                # turn off repeated mode when you hit the character that was repeated
                if s[start] == repeatedChar:
                    repeatedChar = None
                start += 1
                curr_len -= 1
            else:
                if s[end] in letterSet:
                    # turn on repeated mode
                    repeatedChar = s[end]
                else:
                    # add to set and increment length and change max length
                    # if current length is greater
                    letterSet.add(s[end])
                    end += 1
                    curr_len += 1
                    if curr_len > max_len:
                        max_len = curr_len

        return max_len
