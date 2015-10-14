class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterDict = {}
        start, end = 0, 0
        repeatedChar = None
        curr_len, max_len = 0, 0
        
        while start <= end and end < len(s):
            if repeatedChar != None:
                # move up start position removing characters from dict
                letterDict[s[start]] = None
                # turn off repeated mode when you hit the character that was repeated
                if s[start] == repeatedChar:
                    repeatedChar = None
                start += 1
                curr_len -= 1
            else:
                if s[end] in letterDict and letterDict[s[end]] != None:
                    # turn on repeated mode
                    repeatedChar = s[end]
                else:
                    # add to dictionary and increment length and change max length
                    # if current length is greater
                    letterDict[s[end]] = True
                    end += 1
                    curr_len += 1
                    if curr_len > max_len:
                        max_len = curr_len
                        
        return max_len
