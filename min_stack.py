
"""
A stack where you can also keep track of the minimum
A minimum stack has to keep track of count because if you have 
1 1 3 1 and you pop off the 1, if you don't keep track of the count for 
the minimum stack, you will say 3 is the minimum even though there are other 1's 
that are duplicates
"""

class Node:
    """
    A linked-list node for the main stack
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MinNode:
    """
    A linked-list node for the minimum stack
    Includes a count to make sure that duplicates will also count for the minimum
    """
    def __init__(self, data):
        self.data = data
        self.count = 1
        self.next = None

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.front = None
        self.minfront = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        addedNode = Node(x)
        
        if self.front == None:
            self.front = addedNode
        else:
            oldFront = self.front
            self.front = addedNode
            self.front.next = oldFront
            
        if self.minfront != None and x < self.minfront.data:
            oldMinFront = self.minfront
            self.minfront = MinNode(x)
            self.minfront.next = oldMinFront
        elif self.minfront == None:
            self.minfront = MinNode(x)
        elif x == self.minfront.data:
            self.minfront.count += 1

    def pop(self):
        """
        :rtype: nothing
        """
        if self.front != None:
            if self.minfront != None and self.minfront.data == self.front.data:
                self.minfront.count -= 1
                if self.minfront.count == 0:
                    self.minfront = self.minfront.next
            
            retVal = self.front.data
            self.front = self.front.next
            return retVal
        return None

    def top(self):
        """
        :rtype: int
        """
        if self.front != None:
            return self.front.data
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.minfront != None:
            return self.minfront.data
        return None
