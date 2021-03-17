class trieNode:
    def __init__(self, l):
        self.l=l
        self.end=False
        self.children={}

    
def noPrefix(words):
    root=trieNode("0")
    # Write your code here
    for word in words:
        result = notPre(word,root)
        if not result:
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")

def notPre(word, node):
    if word[0] in node.children:
        if node.children[word[0]].end==True:
            return False
        if len(word)==1:
            return False
        return notPre(word[1:],node.children[word[0]])
    
    node.children[word[0]]=trieNode(word[0])
    if len(word)==1:
        node.children[word[0]].end=True
        return True
    return notPre(word[1:],node.children[word[0]])
