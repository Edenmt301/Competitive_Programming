class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned=set(banned)
        symbols="!?',;."
        for s in symbols:
            paragraph=paragraph.replace(s," ")
        
        par=paragraph.split()
        words={}
        answer=""
                
        for i in par:
            word=""
            for x in range(len(i)):
                each=i[x]
                if ord(each)<91 and ord(each)>64:
                    word += chr(ord(each) + 32)
                elif ord(each)<123 and ord(each)>96:
                    word +=each
                else:
                    if each!=i[-1]:
                        par.append(i[x+1:])
            if word not in banned:
                answer=word
            if word not in words:
                words[word]=1
                continue
            words[word]+=1
        
        for key in words:
            if words[key]>words[answer] and key not in banned:
                answer=key
      
        return answer
