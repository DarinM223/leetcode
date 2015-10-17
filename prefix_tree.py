class TrieNode(object):
    """
    A node that contains the letter contained by the trie
    and a dictionary of children
    """
    
    def __init__(self, letter):
        """
        Initialize your data structure here.
        """
        self.letter = letter
        self.children = {}

class Trie(object):
    """
    
    Trie made by creating nodes for each letter and a end marker at the end
    
    Examples: insert("ab")
    Result trie:
    a
    |
    b
    |
    end
    
    insert("ab"), insert("abc"):
      a
      |
      b
    |    |
    end  c
    
    """

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        currentWord = word
        
        while len(currentWord) > 0:
            ch = currentWord[0]
            
            if not ch in node.children:
                node.children[ch] = TrieNode(ch)
                
            node = node.children[ch]
            
            currentWord = currentWord[1:]
        
        node.children['END'] = TrieNode('END')

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        currentWord = word
        
        while len(currentWord) > 0:
            ch = currentWord[0]
            
            if not ch in node.children:
                return False
                
            node = node.children[ch]
            
            currentWord = currentWord[1:]
            
        return 'END' in node.children

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        currentWord = prefix
        while len(currentWord) > 0:
            ch = currentWord[0]
            
            if not ch in node.children:
                return False
            
            node = node.children[ch]
            
            currentWord = currentWord[1:]
        
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
