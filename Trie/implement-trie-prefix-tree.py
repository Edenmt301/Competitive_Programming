class Node:
    def __init__(self, l):
        self.letter= l
        self.end= False
        self.children={}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root= Node("0")
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current= self.root
        
        for i in word:
            if i not in current.children:
                current.children[i]= Node(i)
            current=current.children[i]
        current.end=True
                
    def getNode(self, word: str):
        current= self.root
        for i in word:
            if i in current.children:
                current=current.children[i]
            else:
                return None
        return current
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if self.getNode(word) and self.getNode(word).end:
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if self.getNode(prefix):
            return True
        return False
