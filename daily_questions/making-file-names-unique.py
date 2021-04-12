#https://leetcode.com/problems/making-file-names-unique

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        newList = []
        words = dict()
        for i in names:
                if i not in words:
                    words[i]=0
                    newList.append(i)
                else:
                    words[i]+=1
                    newWord = i + "(" + str(words[i]) + ")"
                    while(newWord in words):
                        words[i] += 1
                        newWord = i +"(" + str(words[i]) + ")"
                        
                    words[newWord]=0
                    newList.append(newWord)
        return newList
