class trieNode:
    def __init__(self,letter):
        self.letter=letter
        self.end=False
        self.children={}
        

class Solution: 
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words= sentence.split()
        root=trieNode(" ")
        for i in dictionary:
            temp=root
            self.insert(temp,i)
        for index in range(len(words)):
            temp=root
            if not self.findroot(temp, words[index]):
                continue
            words[index]=self.findroot(temp,words[index])
        return " ".join(words)
          
    def insert(self, root, word):
        if word[0] not in root.children:
            root.children[word[0]]=trieNode(word[0])
        if len(word)==1:
            root.children[word[0]].end=True
            return 
        return self.insert(root.children[word[0]],word[1:])
                
            
    def findroot(self, root, word, pre = ""):
        if word:
            if word[0] in root.children:
                pre+=word[0]
                if root.children[word[0]].end:
                    return pre
                return self.findroot(root.children[word[0]], word[1:], pre)
        return None
