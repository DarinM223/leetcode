# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # Time complexity (n * m) ^ 2
        
        # add all elements into a heap and then
        # pop them off into the result array
        heap = []
        for l in lists:
            while l is not None:
                heapq.heappush(heap, l.val)
                l = l.next
        
        result = []
        while len(heap) != 0:
            result.append(heapq.heappop(heap))
            
        return result
