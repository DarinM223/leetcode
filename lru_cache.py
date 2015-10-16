class Node:
    """
    Node for a doubly-linked-list that holds the key used to 
    index in the hashmap and the value for the key
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):
    """
    Implemented as a doubly linked-list used as a "queue" containing the nodes and
    a hashmap containing the key-node pairs
    
    When you get a key, the node with the key gets moved to the front of the queue
    
    When you set a key and have to evict, you evict from the rear of the queue and
    add the new node to the front of the queue
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.front = None
        self.rear = None
        self.pageMap = {}
        
    def remove(self, n):
        if n.prev:
            n.prev.next = n.next
        else:
            self.rear = n.next
            
        if n.next:
            n.next.prev = n.prev
        else:
            self.front = n.prev
            
    def addToFront(self, n):
        n.next = None
        n.prev = self.front
        if self.rear == None:
            self.rear = n
        else:
            self.front.next = n
        self.front = n

    def get(self, key):
        """
        :rtype: int
        """
        if not key in self.pageMap or self.pageMap[key] == None:
            return -1
        
        # move the node with the key to the top of the queue
        node = self.pageMap[key]
        if node != self.front:
            # if node is not in the front remove it and add to front of queue
            self.remove(node)
            self.addToFront(node)
            
        return node.value
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        # don't forget to check the case where the key is already in the hashmap
        if key in self.pageMap and self.pageMap[key] != None:
            # remove the node
            node = self.pageMap[key]
            self.remove(node)
            
            # set the hashmap with the new node and add the new node to the front of the queue
            newNode = Node(key, value)
            self.pageMap[key] = newNode
            self.addToFront(newNode)
        else:
            if self.count == self.capacity:
                # if full, remove rear key from hash
                self.pageMap[self.rear.key] = None
                # and evict rear node from queue
                self.remove(self.rear)
                self.count -= 1
        
            # add new node to the front of the queue
            newFront = Node(key, value)
            self.addToFront(newFront)
        
            # add the key-value pair to the map
            self.pageMap[key] = newFront
        
            self.count += 1
