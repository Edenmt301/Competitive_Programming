class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana={}
        for i in strs:
            key="".join((sorted(i)))
            if key in ana:
                ana[key].append(i)
                continue
            ana[key]=[i]
            
        answer=[]
        for i in ana:
            answer.append(ana[i])
        return answer
